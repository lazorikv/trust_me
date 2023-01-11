from flask import Blueprint, make_response, jsonify, request
from sqlalchemy import desc, asc
from app import db
from app.apartment.schemas import ApartmentPostSchema, ApartmentListSchema, ApartmentPatchSchema
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
            description = data.get("description", None)
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
                                  address_id=address.id, landlord_id=current_user.id, description=description)
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
        return make_response({f"message": f'Deleted'}, 202)
    elif method in ("PATCH",):
        data = request.get_json()
        result = ApartmentPatchSchema().load(data, partial=True)
        apartment = Apartment.query.filter_by(id=apartment_id).first()
        tenant_id = result.get("tenant_id", None)
        area = result.get("area", None)
        floor = result.get("floor", None)
        room_count = result.get("room_count", None)
        cost = result.get("cost", None)
        description = result.get("description", None)
        if area:
            apartment.area = area
        if floor:
            apartment.floor = floor
        if room_count:
            apartment.room_count = room_count
        if cost:
            apartment.cost = cost
        if description:
            apartment.description = description

        landlord_id = result.get("landlord_id", None)
        address = result.get("address", None)
        if current_user.id != landlord_id:
            return make_response({"error": "Patch Apartment can only Landlord user"}, 400)

        if address:
            address_exist = Address.query.get(apartment.address_id)
            db.session.delete(address_exist)
            address = Address(city=address.get("city", None),
                              district=address.get("district", None),
                              street=address.get("street", None),
                              house_number=address.get("house_number", None),
                              apart_number=address.get("apart_number", None))
            db.session.add(address)
            db.session.commit()
            apartment.address_id = address.id

        if tenant_id:
            apartment.tenant_id = tenant_id
        if landlord_id:
            apartment.landlord_id = landlord_id

        db.session.commit()
        return ApartmentListSchema().dump(apartment)


@mod.route("/search", methods=["GET"])
def apartment_search():
    args = request.args
    city = args.get("city")
    page = args.get("page", 1)
    per_page = 10
    apartment = Apartment.query.order_by(asc(Apartment.cost))
    if city:
        apartment = apartment.join(Address).filter(Address.city == city)
    if page:
        total = apartment.count()
        apartment = apartment.paginate(page=int(page), per_page=per_page, error_out=False)

    return make_response({"apartments": ApartmentListSchema(many=True).dump(apartment), "total": total})
