from marshmallow import Schema, fields
from app.apartment.schemas import ApartmentListSchema
from app.contract.schemas import ContractTenantSchema


class TenantPostSchema(Schema):

    email = fields.Email()
    first_name = fields.Str()
    last_name = fields.Str()
    phone_number = fields.Str()


class TenantGetSchema(TenantPostSchema):

    apartment = fields.Nested(ApartmentListSchema)
    contract = fields.Nested(ContractTenantSchema)
    created_at = fields.Str()
    updated_at = fields.Str()


class TenantListSchema(TenantGetSchema):

    id = fields.Int()


class TenantCutSchema(Schema):
    id = fields.Int()
    email = fields.Email()
    first_name = fields.Str()
    last_name = fields.Str()
    phone_number = fields.Str()