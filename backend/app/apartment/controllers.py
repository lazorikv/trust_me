from flask import Blueprint, make_response, jsonify, request
from app import db
from app.apartment.schemas import ApartmentPostSchema, ApartmentListSchema
from app.auth.utils import token_required
from app.models import Landlord, Apartment, Contract, Address


mod = Blueprint('apartments', __name__, url_prefix='/apartment')


@mod.route('/', methods=['GET', "POST"])
@token_required
def apartment_func(current_user):

    method = request.method
    if method in ("GET",):
        apartments = Apartment.query.all()
        return ApartmentListSchema(many=True).dump(apartments)

    elif method in ("POST",):
        if type(current_user) is not Landlord:
            return make_response({"error": "Create Apartment can only Landlord user"}, 400)
        data = request.get_json()
        data = ApartmentPostSchema().load(data)
        if data:
            floor = data.get("floor", None)
            room_count = data.get("room_count", None)
            area = data.get("area", None)
            cost = data.get("cost", None)
            is_rented = data.get("is_rented", False)
            address_data = data.get("address", None)

            address = Address(city=address_data.get("city", None),
                              district=address_data.get("district", None),
                              street=address_data.get("street", None),
                              house_number=address_data.get("house_number", None),
                              apart_number=address_data.get("apart_number", None))
            db.session.add(address)
            db.session.commit()
            apartment = Apartment(floor=floor, room_count=room_count, area=area, cost=cost, is_rented=is_rented,
                                  address_id=address.id, landlord_id=current_user.id)
            db.session.add(apartment)

            db.session.commit()
            return ApartmentListSchema().dump(apartment)


@mod.route("/<apartment_id>", methods=["PATCH", "DELETE"])
@token_required
def apart_func(current_user, apartment_id):
    method = request.method
    apartment = Apartment.query.filter_by(id=apartment_id).first()
    if method in ('GET',):
        return ApartmentListSchema().dump(apartment)
    elif method in ('DELETE',):
        contracts = Contract.query.filter_by(id=apartment.contract.id)
        for contract in contracts:
            contract.delete_contract()
        db.session.delete(contracts)
        # photos = ApartmentPhoto.query.filter_by(id=apartment.photo.id)
        # db.session.delete(photos)
        db.session.delete(apartment)
        db.session.commit()
        return make_response({f"message": f'{response}'}, 202)
    elif method in ("PATCH",):
        data = request.form
        result = ContractPatchSchema().load(data, partial=True)
        url = result.get("url", None)
        tenant_id = result.get("tenant_id", None)
        landlord_id = result.get("landlord_id", None)
        apartment_id = result.get("apartment_id", None)
        if url:
            contract.url = url
        else:
            file = request.files.get("contract_file", None)
            if file:
                old_filename = contract.url
                old_filename = old_filename.split(".com/")[-1]
                bucket.delete_file(key=old_filename)
                file.filename = secure_filename(file.filename)
                file.filename = f"{current_user.id}/{file.filename}"
                filename = bucket.upload_file_to_s3(file)
                url = f"https://lazoryktrust.s3.us-east-1.amazonaws.com/{filename}"
                contract.url = url

        if tenant_id:
            contract.tenant_id = tenant_id
        if apartment_id:
            contract.apartment_id = apartment_id
        if landlord_id:
            contract.landlord_id = landlord_id
        return ContractListSchema().dump(contract)
