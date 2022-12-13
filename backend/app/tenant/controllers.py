from flask import Blueprint, make_response, request
from app import db
from marshmallow import ValidationError
from .schemas import TenantListSchema, TenantPostSchema, TenantGetSchema
from app.models import Tenant, Apartment, Contract


mod = Blueprint('tenants', __name__, url_prefix='/tenant')


@mod.route('/', methods=['GET'])
def tenant_func():
    method = request.method
    if method in ("GET",):
        tenants = Tenant.query.all()
        return TenantListSchema(many=True).dump(tenants)


@mod.route('/<tenant_id>', methods=["GET", "PUT", "PATCH", "DELETE"])
def change_tenant(tenant_id):
    method = request.method
    tenant = Tenant.query.get(tenant_id)
    if tenant:
        if method in ("DELETE",):
            db.session.delete(tenant)
            db.session.commit()
            return make_response({"message": 'Tenant deleted'}, 202)
        elif method in ("PUT", "PATCH"):
            data = request.get_json()
            if data:
                schema = TenantPostSchema()
                try:
                    data = schema.load(data)
                except ValidationError as error:
                    return make_response({"error": error.messages}, 400)
                tenant.email = data["email"]
                tenant.first_name = data["first_name"]
                tenant.last_name = data["last_name"]
                tenant.phone_number = data["phone_number"]

                apartment_data = data.get("apartment", None)
                if apartment_data:
                    apartment = Apartment.query.get(id=apartment_data["id"])
                    tenant.apartment.add(apartment)

                contract_data = data.get("contract", None)
                if contract_data:
                    contract = Contract.query.get(id=contract_data["id"])
                    tenant.apartment.add(contract)
                db.session.add(tenant)
                db.session.commit()
                return TenantGetSchema().dump(tenant)
            return make_response('No data', 400)
        elif method in ("GET",):
            return TenantGetSchema().dump(tenant)

    return make_response({"error": f"Tenant with id = {tenant_id} is not exist"}, 404)
