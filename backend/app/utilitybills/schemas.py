from marshmallow import Schema, fields
from app.apartment.schemas import ApartmentListSchema


class UtilityBillsPostSchema(Schema):

    gas = fields.Float()
    water = fields.Float()
    electricity = fields.Float()
    apartment_id = fields.Int()


class UtilityBillsGetSchema(UtilityBillsPostSchema):

    apartment = fields.Nested(ApartmentListSchema)
    created_at = fields.Str()
    updated_at = fields.Str()


class UtilityBillsListSchema(UtilityBillsGetSchema):

    id = fields.Int()


class UtilityBillsCutSchema(Schema):

    id = fields.Int()
    gas = fields.Float()
    water = fields.Float()
    electricity = fields.Float()
    apartment_id = fields.Int()
