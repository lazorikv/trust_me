from flask import Blueprint, make_response, jsonify, request
from app.apartment.schemas import AddressSchema, AddressListSchema
from app.models import Address
from app.auth.utils import token_required


mod = Blueprint('addresses', __name__, url_prefix='/address')


@mod.route('/', methods=['GET'])
@token_required
def address_func(current_user):
    method = request.method
    if method in ("GET", ):
        addresses = Address.query.all()
        address_schema = AddressListSchema(many=True)
        result = address_schema.dump(addresses)
        return result


@mod.route('/<address_id>', methods=['GET'])
@token_required
def address_part_func(current_user, address_id):
    method = request.method
    address = Address.query.filter_by(id=address_id).first()
    if method in ('GET', ):
        return AddressListSchema().dump(address)


