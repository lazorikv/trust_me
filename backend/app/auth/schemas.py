from marshmallow import Schema, fields


class SignUpSchema(Schema):

    role = fields.Str()
    email = fields.Str()
    password = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    phone_number = fields.Str()


class LoginSchema(Schema):

    role = fields.Str()
    email = fields.Str()
    password = fields.Str()


class ChangePasswordSchema(Schema):
    role = fields.Str()
    password = fields.Str()
    old_password = fields.Str()

