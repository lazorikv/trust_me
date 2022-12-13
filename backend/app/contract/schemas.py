from marshmallow import Schema, fields


class ContractCutSchema(Schema):

    id = fields.Int()
    url = fields.Str()


class ContractPatchSchema(Schema):
    contract_file = fields.Raw(type='file')
    tenant_id = fields.Int()
    landlord_id = fields.Int()
    apartment_id = fields.Int()


class ContractListSchema(ContractCutSchema):

    tenant_id = fields.Int()
    landlord_id = fields.Int()
    apartment_id = fields.Int()
    created_at = fields.Str()
    updated_at = fields.Str()


class ContractLandlordSchema(ContractCutSchema):

    tenant_id = fields.Str()
    apartment_id = fields.Str()
    created_at = fields.Str()
    updated_at = fields.Str()


class ContractTenantSchema(ContractCutSchema):

    landlord_id = fields.Int()
    apartment_id = fields.Int()
    created_at = fields.Str()
    updated_at = fields.Str()

