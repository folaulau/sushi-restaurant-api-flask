from app import db
from json import JSONEncoder
from app.utils.custom_serializer_mixin import CustomSerializerMixin


# class User(db.Model, CustomSerializerMixin):
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer, primary_key=True)
#     uuid = db.Column(db.String(255), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     first_name = db.Column(db.String(250), nullable=True)
#     last_name = db.Column(db.String(250), nullable=True)
#     phone_number = db.Column(db.String(250), nullable=True)
#     dob = db.Column(db.DATETIME, nullable=True)
#     email_temp = db.Column(db.BOOLEAN, nullable=True)
#     deleted = db.Column(db.BOOLEAN, nullable=True)
#     created_at = db.Column(db.DATETIME, nullable=True)
#     updated_at = db.Column(db.DATETIME, nullable=True)
#     status = db.Column(db.String(50), nullable=True)
#     account_id = db.Column(db.Integer, db.ForeignKey('user.id'),
#         nullable=False)
#
#     # select fields to serialize from object to dict
#     serialize_only = ('id', 'uuid', 'email', 'first_name', 'last_name','phone_number','dob',
#                       'email_temp','deleted','created_at','updated_at','status','account_id')
#
#     def __init__(self, uuid, email, first_name, last_name, phone_number, dob, email_temp, deleted, created_at
#                  , updated_at, status):
#         self.uuid = uuid
#         self.email = email
#         self.first_name = first_name
#         self.last_name = last_name
#         self.phone_number = phone_number
#         self.dob = dob
#         self.email_temp = email_temp
#         self.deleted = deleted
#         self.created_at = created_at
#         self.updated_at = updated_at
#         self.status = status
#
#
# class UserEncoder(JSONEncoder):
#     def default(self, obj):
#         return obj.__dict__
