from marshmallow import Schema, fields
from app.contract.schemas import ContractListSchema, ContractLandlordSchema, ContractTenantSchema


class AddressSchema(Schema):

    city = fields.Str()
    district = fields.Str()
    street = fields.Str()
    house_number = fields.Int()
    apart_number = fields.Int()


class AddressListSchema(AddressSchema):

    id = fields.Int()


class ApartmentPostSchema(Schema):

    floor = fields.Int()
    room_count = fields.Int()
    area = fields.Float()
    cost = fields.Float()
    is_rented = fields.Boolean()
    address = fields.Nested(AddressSchema)
    description = fields.Str()
    landlord_id = fields.Int()


class ApartmentPatchSchema(ApartmentPostSchema):
    id = fields.Int()


class ApartmentGetSchema(Schema):
    floor = fields.Int()
    room_count = fields.Int()
    area = fields.Float()
    cost = fields.Float()
    is_rented = fields.Boolean()
    description = fields.Str()
    contract = fields.Nested(ContractListSchema)
    address = fields.Nested(AddressListSchema)
    landlord_id = fields.Int()
    tenant_id = fields.Int()
    created_at = fields.DateTime(format="timestamp")
    # photo = fields.Nested(ApartmentPhotoSchema)


class ApartmentListSchema(ApartmentGetSchema):

    id = fields.Int()
