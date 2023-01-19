from marshmallow import Schema, fields
from app.contract.schemas import ContractListSchema, ContractLandlordSchema, ContractTenantSchema
from app.apartment_photo.schemas import ApartmentPhotoListSchema
from app.models import Apartment

class AddressSchema(Schema):

    city = fields.Str()
    district = fields.Str()
    street = fields.Str()
    house_number = fields.Int()
    apart_number = fields.Int()


class UserApartmentSchema(Schema):
    email = fields.Email()
    first_name = fields.Str()
    last_name = fields.Str()
    phone_number = fields.Str()
    created_at = fields.DateTime(format="timestamp")
    updated_at = fields.DateTime(format="timestamp")
    apartment_count = fields.Method("get_apartment_count")

    def get_apartment_count(self, obj):
        apartment_count = Apartment.query.filter_by(landlord_id=obj.id).count()
        return apartment_count


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
    title = fields.Str()
    area = fields.Float()
    cost = fields.Float()
    is_rented = fields.Boolean()
    description = fields.Str()
    contract = fields.List(fields.Nested(ContractListSchema, exclude=("apartment_id",)))
    address = fields.Nested(AddressListSchema)
    landlord = fields.Nested(UserApartmentSchema)
    tenant = fields.Nested(UserApartmentSchema)
    created_at = fields.DateTime(format="timestamp")
    photo = fields.List(fields.Nested(ApartmentPhotoListSchema))


class ApartmentListSchema(ApartmentGetSchema):

    id = fields.Int()
