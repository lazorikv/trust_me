# -*-coding:utf-8-*-
import uuid
from flask import (Blueprint, request, jsonify, make_response)
import jwt
from flask_expects_json import expects_json
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app
from app import db
from app.models import Landlord, Tenant
from app.tenant.schemas import TenantGetSchema
from app.landlord.schemas import LandlordGetSchema
from .schemas import SignUpSchema, LoginSchema, ChangePasswordSchema


mod = Blueprint('auth', __name__, url_prefix='/auth')


# register route
@mod.route('/signup', methods=['POST'])
def signup_user():
    data = request.get_json()
    data = SignUpSchema().load(data)
    role = data.get("role", None)
    if not role:
        return make_response(jsonify({"error": "Field role is required"}), 400)
    user = None
    if role == "tenant":
        user = Tenant.query.filter_by(email=data['email']).first()
    elif role == "landlord":
        user = Landlord.query.filter_by(email=data['email']).first()
    hashed_password = generate_password_hash(data['password'], method='sha256')

    if not user:
        if role == "tenant":
            new_user = Tenant(public_id=str(uuid.uuid4()),
                              password=hashed_password, email=data['email'],
                              first_name=data["first_name"],
                              last_name=data["last_name"], phone_number=data["phone_number"])
            result = TenantGetSchema().dump(new_user)

        elif role == "landlord":
            new_user = Landlord(public_id=str(uuid.uuid4()),
                                password=hashed_password, email=data['email'],
                                first_name=data["first_name"],
                                last_name=data["last_name"], phone_number=data["phone_number"])
            result = LandlordGetSchema().dump(new_user)
        else:
            return make_response(jsonify({"error": "Field role is required"}), 400)

        db.session.add(new_user)
        db.session.commit()

        return result
    else:
        return make_response(jsonify({"message": "User already exists!"}), 409)


# user login route
@mod.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    auth = LoginSchema().load(auth)
    role = auth.get("role", None)
    if not auth or not auth.get('email', None) or not auth.get('password', None) or not role:
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic-realm= "Login required!"'})
    user = None
    if role == "tenant":
        user = Tenant.query.filter_by(email=auth['email']).first()
    elif role == "landlord":
        user = Landlord.query.filter_by(email=auth['email']).first()
    if not user:
        return make_response('Could not verify user!', 401, {'WWW-Authenticate': 'Basic-realm= "No user found!"'})
    if check_password_hash(user.password, auth.get('password')):
        token = jwt.encode({'public_id': user.public_id}, current_app.config['SECRET_KEY'], 'HS256')
        return make_response(jsonify({'token': token, "success": True, "message": "Success"}), 201)

    return make_response('Could not verify password!', 403, {'WWW-Authenticate': 'Basic-realm= "Wrong Password!"'})


@mod.route("/change_password/<user_id>", methods=["POST"])
def change_password(user_id):
    auth = request.get_json()
    auth = ChangePasswordSchema().load(auth)
    role = auth.get("role", None)
    if not auth or not auth.get('new_password') or not auth.get('old_password') or not role:
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic-realm= "Login required!"'})
    user = None
    if role == "tenant":
        user = Tenant.query.filter_by(id=user_id).first()
    elif role == "landlord":
        user = Landlord.query.filter_by(id=user_id).first()
    if not user:
        return make_response('Could not verify user!', 401, {'WWW-Authenticate': 'Basic-realm= "No user found!"'})
    if check_password_hash(user.password, auth.get('old_password')):
        hashed_password = generate_password_hash(auth['new_password'], method='sha256')
        user.password = hashed_password
        db.session.add(user)
        db.session.commit()
        return make_response('Password changed', 201)
    return make_response('Old password is incorrect!', 401, {'WWW-Authenticate': 'Basic-realm= "No user found!"'})


@mod.route("/time", methods=["GET"])
def time():
    return make_response({"time": 'Could not verify password!'}, 200)
