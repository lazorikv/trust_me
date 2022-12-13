from flask import Blueprint, make_response, request
from app import db
from app import bucket
from app.contract.schemas import ContractListSchema, ContractCutSchema, ContractPatchSchema
from app.models import Landlord, Apartment, Contract
from app.auth.utils import token_required

from werkzeug.utils import secure_filename


mod = Blueprint('contracts', __name__, url_prefix='/contract')


@mod.route('/', methods=['GET', 'POST'])
@token_required
def contract_func(current_user):
    method = request.method
    if method in ("GET", ):
        contracts = Contract.query.all()
        contract_schema = ContractListSchema(many=True)
        result = contract_schema.dump(contracts)
        return result
    elif method in ('POST',):
        if "contract_file" not in request.files:
            return "No contract_file key in request.files"

        file = request.files["contract_file"]

        if file.filename == "":
            return "Please select a file"

        file.filename = secure_filename(file.filename)
        file.filename = f"contracts/{current_user.id}/{file.filename}"
        filename = bucket.upload_file_to_s3(file)
        url = f"https://lazoryktrust.s3.us-east-1.amazonaws.com/{filename}"

        contract = Contract(url=url, apartment_id=request.form["apartment_id"],
                            tenant_id=request.form["tenant_id"],
                            landlord_id=request.form["landlord_id"])
        db.session.add(contract)
        db.session.commit()
        return ContractListSchema().dump(contract)


@mod.route('/<contract_id>', methods=['PATCH', 'GET', 'DELETE'])
@token_required
def contract_part_func(current_user, contract_id):
    method = request.method
    contract = Contract.query.filter_by(id=contract_id).first()
    if method in ('GET', ):
        return ContractCutSchema().dump(contract)
    elif method in ('DELETE',):
        filename = request.form["filename"]
        filename = f"contracts/{current_user.id}/{filename}"
        # !IMPORTANT! : User access must be checked before delete operation!
        response = bucket.delete_file(filename)
        db.session.delete(contract)
        db.session.commit()
        return make_response({f"message": f'{response}'}, 202)
    elif method in ("PATCH",):
        data = request.form
        result = ContractPatchSchema().load(data, partial=True)
        url = result.get("url", None)
        tenant_id = result.get("tenant_id", None)
        landlord_id = result.get("landlord_id", None)
        apartment_id = result.get("apartment_id", None)
        if url:
            contract.url = url
        else:
            file = request.files.get("contract_file", None)
            if file:
                contract.delete_contract()
                file.filename = secure_filename(file.filename)
                file.filename = f"contracts/{current_user.id}/{file.filename}"
                filename = bucket.upload_file_to_s3(file)
                url = f"https://lazoryktrust.s3.us-east-1.amazonaws.com/{filename}"
                contract.url = url

        if tenant_id:
            contract.tenant_id = tenant_id
        if apartment_id:
            contract.apartment_id = apartment_id
        if landlord_id:
            contract.landlord_id = landlord_id
        return ContractListSchema().dump(contract)

