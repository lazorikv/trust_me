# -*- coding:utf-8 -*-
from app import db
from app import bucket


class Address(db.Model):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    apartment = db.relationship('Apartment', backref='address', lazy='dynamic')
    city = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    house_number = db.Column(db.Integer, nullable=False)
    apart_number = db.Column(db.Integer, nullable=True)

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<City {self.city} district {self.district} street {self.street} house number ' \
               f'{self.house_number}> apartment number {self.apart_number}'


class Tenant(db.Model):
    __tablename__ = 'tenant'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(255))
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(100), nullable=False)

    apartment = db.relationship('Apartment', backref='tenant', lazy='dynamic')
    contract = db.relationship('Contract', backref='tenant', lazy='dynamic')

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __str__(self):
        return "Tenant"


class Landlord(db.Model):
    __tablename__ = 'landlord'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(255))
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(100), nullable=False)

    apartment = db.relationship('Apartment', backref='landlord', lazy='dynamic')
    contract = db.relationship('Contract', backref='landlord', lazy='dynamic')

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return self

    def __str__(self):
        return "Landlord"


class Apartment(db.Model):
    __tablename__ = "apartment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    floor = db.Column(db.Integer, nullable=False)
    room_count = db.Column(db.Integer, nullable=False)
    area = db.Column(db.Float, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    title = db.Column(db.Text, nullable=True)
    is_rented = db.Column(db.Boolean, nullable=False, default=False)

    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'), nullable=True)
    landlord_id = db.Column(db.Integer, db.ForeignKey('landlord.id'), nullable=True)
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=True)

    utility_bills = db.relationship('UtilityBills', backref='apartment', lazy='dynamic')
    contract = db.relationship('Contract', backref='apartment', lazy='dynamic')
    photo = db.relationship('ApartmentPhoto', backref='apartment', lazy='dynamic')

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return self


class Contract(db.Model):
    __tablename__ = "contract"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(255), nullable=False)

    landlord_id = db.Column(db.Integer, db.ForeignKey('landlord.id'), nullable=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'), nullable=True)
    apartment_id = db.Column(db.Integer, db.ForeignKey("apartment.id"), nullable=True)

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def delete_contract(self):
        old_filename = self.url.split(".com/")[-1]
        bucket.delete_file(key=old_filename)


class UtilityBills(db.Model):
    __tablename__ = "utility_bills"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gas = db.Column(db.Float, nullable=False)
    water = db.Column(db.Float, nullable=False)
    electricity = db.Column(db.Float, nullable=False)

    apartment_id = db.Column(db.Integer, db.ForeignKey("apartment.id"), nullable=True)

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


class ApartmentPhoto(db.Model):
    __tablename__ = "photo"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(255), nullable=False)
    apartment_id = db.Column(db.Integer, db.ForeignKey("apartment.id"), nullable=True)

    def delete_photo(self):
        old_filename = self.url.split(".com/")[-1]
        bucket.delete_file(key=old_filename)
        return "Success"
