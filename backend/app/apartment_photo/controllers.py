from flask import Blueprint, make_response, request
from app import db
from app import bucket
from app.apartment_photo.schemas import ApartmentPhotoListSchema, ApartmentPhotoCutSchema, ApartmentPhotoPatchSchema
from app.models import Landlord, Apartment, ApartmentPhoto
from app.auth.utils import token_required

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
            return "No photo_files key in request.files"

        files = request.files.getlist("photo_files")

        if len(files) == 0:
            return "Please select a files"

        for file in files:
            file.filename = secure_filename(file.filename)
            file.filename = f"photos/{current_user.id}/{file.filename}"
            bucket.upload_file_to_s3(file)

        url = f"https://lazoryktrust.s3.us-east-1.amazonaws.com/photos/{current_user.id}"

        photos = ApartmentPhoto(url=url, apartment_id=request.form["apartment_id"])
        db.session.add(photos)
        db.session.commit()
        return ApartmentPhotoListSchema().dump(photos)


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
            photos.delete_photos()
            files = request.files.getlist("photo_files")
            if files:
                for file in files:
                    file.filename = secure_filename(file.filename)
                    file.filename = f"photos/{current_user.id}/{file.filename}"
                    bucket.upload_file_to_s3(file)
                url = f"https://lazoryktrust.s3.us-east-1.amazonaws.com/photos/{current_user.id}/"
                photos.url = url

        if apartment_id:
            photos.apartment_id = apartment_id

        return ApartmentPhotoListSchema().dump(photos)

