from flask import Blueprint, make_response, request
from marshmallow import ValidationError
from app import db
from app.models import Landlord, Apartment, Contract
from app.auth.utils import token_required
from .schemas import LandlordPostSchema, LandlordListSchema, LandlordGetSchema


mod = Blueprint('landlords', __name__, url_prefix='/landlord')


@mod.route('/', methods=['GET'])
@token_required
def landlord_func(current_user):
    method = request.method
    if method in ("GET", ):
        landlords = Landlord.query.all()
        return LandlordListSchema(many=True).dump(landlords)


@mod.route('/<landlord_id>', methods=["GET", "PUT", "PATCH", "DELETE"])
@token_required
def change_landlord(current_user, landlord_id):
    method = request.method
    landlord = Landlord.query.get(landlord_id)
    if landlord:
        if method in ("DELETE", ):
            db.session.delete(landlord)
            db.session.commit()
            return make_response({f"message": f'Landlord with id = {landlord_id} deleted'}, 202)
        elif method in ("PUT", "PATCH"):
            data = request.get_json()
            if data:
                schema = LandlordPostSchema()
                try:
                    data = schema.load(data)
                except ValidationError as error:
                    return make_response({"error": error.messages}, 400)
                landlord.email = data["email"]
                landlord.first_name = data["first_name"]
                landlord.last_name = data["last_name"]
                landlord.phone_number = data["phone_number"]
                apartment_data = data.get("apartment", None)
                if apartment_data:
                    apartment = Apartment.query.get(id=apartment_data["id"])
                    landlord.apartment.add(apartment)
                contract_data = data.get("contract", None)
                if contract_data:
                    contract = Contract.query.get(id=contract_data["id"])
                    landlord.apartment.add(contract)
                db.session.add(landlord)
                db.session.commit()
                return LandlordListSchema().dump(landlord)
            return make_response('No data', 400)
        elif method in ("GET",):
            return LandlordGetSchema().dump(landlord)

    return make_response({"error": f"Landlord with id = {landlord_id} is not exist"}, 404)

