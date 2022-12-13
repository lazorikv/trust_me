from flask import Blueprint, make_response, request
from app import db
from marshmallow import ValidationError
from .schemas import UtilityBillsPostSchema, UtilityBillsGetSchema, UtilityBillsListSchema
from app.models import Tenant, Apartment, Contract, UtilityBills


mod = Blueprint('utilitybills', __name__, url_prefix='/utilitybills')


@mod.route('/', methods=['GET', "POST"])
def utilitybills_func():
    method = request.method
    if method in ("GET",):
        utilitybills = UtilityBills.query.all()
        return UtilityBillsListSchema(many=True).dump(utilitybills)
    elif method in ("POST",):
        data = request.get_json()
        data = UtilityBillsPostSchema().load(data)
        ubills = None
        if data:
            ubills = UtilityBills(gas=data.get("gas"),
                                  water=data.get("water"),
                                  electricity=data.get("electricity"),
                                  apartment_id=data.get("apartment_id"))
            db.session.add(ubills)
            db.session.commit()
        return UtilityBillsGetSchema().dump(ubills)


@mod.route('/<utilitybills_id>', methods=["GET", "PATCH", "DELETE"])
def change_utilitybills(utilitybills_id):
    method = request.method
    utilitybills = UtilityBills.query.get(utilitybills_id)
    if utilitybills:
        if method in ("DELETE",):
            db.session.delete(utilitybills)
            db.session.commit()
            return make_response({"message": 'UBills deleted'}, 202)
        elif method in ("PATCH",):
            data = request.get_json()
            if data:
                schema = UtilityBillsPostSchema()
                try:
                    data = schema.load(data)
                except ValidationError as error:
                    return make_response({"error": error.messages}, 400)
                utilitybills.gas = data.get("gas")
                utilitybills.water = data.get("water")
                utilitybills.electricity = data.get("electricity")

                apartment_id = data.get("apartment_id", None)
                if apartment_id:
                    utilitybills.apartment_id = apartment_id

                db.session.add(utilitybills)
                db.session.commit()
                return UtilityBillsGetSchema().dump(utilitybills)
            return make_response('No data', 400)
        elif method in ("GET",):
            return UtilityBillsListSchema().dump(utilitybills)

    return make_response({"error": f"Tenant with id = {utilitybills_id} is not exist"}, 404)
