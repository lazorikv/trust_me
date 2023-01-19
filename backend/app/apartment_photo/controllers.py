from flask import Blueprint, make_response, request
from app import db
from app import bucket
from app.apartment_photo.schemas import ApartmentPhotoListSchema, ApartmentPhotoCutSchema, ApartmentPhotoPatchSchema
from app.models import Landlord, Apartment, ApartmentPhoto
from app.auth.utils import token_required
from app.utils import save_data_s3

from werkzeug.utils import secure_filename


mod = Blueprint('apart_photos', __name__, url_prefix='/apartmentphotos')


@mod.route('/', methods=['GET', 'POST'])
@token_required
def photo_func(current_user):
    method = request.method
    if method in ("GET", ):
        photos = ApartmentPhoto.query.all()
        photos_schema = ApartmentPhotoListSchema(many=True)
        result = photos_schema.dump(photos)
        return result
    elif method in ('POST',):
        if "photo_files" not in request.files:
            return "No photo_files key in request.files", 400

        files = request.files.getlist("photo_files")

        if len(files) == 0:
            return "Please select a files", 400

        for file in files:
            url = save_data_s3(file, current_user)
            photos = ApartmentPhoto(url=url, apartment_id=request.form["apartment_id"])
            db.session.add(photos)
            db.session.commit()
        photo_apartment = ApartmentPhoto.query.filter_by(apartment_id=request.form["apartment_id"]).all()
        return ApartmentPhotoListSchema(many=True).dump(photo_apartment)


@mod.route('/<photos_id>', methods=['PATCH', 'GET', 'DELETE'])
@token_required
def contract_part_func(current_user, photos_id):
    method = request.method
    photos = ApartmentPhoto.query.filter_by(id=photos_id).first()
    if method in ('GET', ):
        return ApartmentPhotoCutSchema().dump(photos)
    elif method in ('DELETE',):
        # !IMPORTANT! : User access must be checked before delete operation!
        response = photos.delete_photos()
        db.session.delete(photos)
        db.session.commit()
        return make_response({f"message": f'{response}'}, 202)
    elif method in ("PATCH",):
        data = request.form
        result = ApartmentPhotoPatchSchema().load(data, partial=True)
        url = result.get("url", None)
        apartment_id = result.get("apartment_id", None)
        if url:
            photos.url = url
        else:
            photos.delete_photo()
            files = request.files.getlist("photo_files")
            if files:
                for file in files:
                    url = save_data_s3(file, current_user)
                    photos.url = url

        if apartment_id:
            photos.apartment_id = apartment_id

        return ApartmentPhotoListSchema().dump(photos)


@mod.route("/<apartment_id>/photos")
@token_required
def apartmnet_photo_byID(current_user, apartment_id):
    if apartment_id:
        photos = ApartmentPhoto.query.filter_by(apartment_id=apartment_id).all()
        return ApartmentPhotoListSchema(many=True).dump(photos)
    return make_response({"error": "Provide apartment_id"}, 400)
