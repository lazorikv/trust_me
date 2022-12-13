from marshmallow import Schema, fields
from app.apartment.schemas import ApartmentListSchema
from app.contract.schemas import ContractLandlordSchema


class LandlordPostSchema(Schema):

    email = fields.Email()
    first_name = fields.Str()
    last_name = fields.Str()
    phone_number = fields.Str()


class LandlordGetSchema(LandlordPostSchema):

    apartment = fields.Nested(ApartmentListSchema)
    contract = fields.Nested(ContractLandlordSchema)
    created_at = fields.Str()
    updated_at = fields.Str()


class LandlordListSchema(LandlordGetSchema):

    id = fields.Int()


class LandlordCutSchema(Schema):

    id = fields.Int()
    email = fields.Email()
    first_name = fields.Str()
    last_name = fields.Str()
    phone_number = fields.Str()

