from marshmallow import Schema, fields


class ApartmentPhotoCutSchema(Schema):

    id = fields.Int()
    url = fields.Str()


class ApartmentPhotoPatchSchema(Schema):

    photo_file = fields.Raw(type='file')
    apartment_id = fields.Int()


class ApartmentPhotoListSchema(ApartmentPhotoCutSchema):

    apartment_id = fields.Int()
    created_at = fields.Str()
    updated_at = fields.Str()
