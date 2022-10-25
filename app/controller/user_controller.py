from app import app
from flask_restful import request, marshal_with, fields
from app.validation.user_validator import authenticate_schema
from app.validation.validator import Validator
from app.service.UserService import UserService;
from flask import jsonify
from app.utils.model_util import to_dic_dto_list

@app.route('/authenticate', methods=['POST'])
def authenticate():
    app.logger.info('sign up')

    # validation
    payload = request.json

    app.logger.debug("payload={}".format(payload))

    resp = Validator(payload, authenticate_schema)

    if resp is not True:
        return {"message": resp}, 400

    # user_service = UserService()

    # pass off data to service

    # return user_service.sign_up(payload)

    return {"name":"sdf"},200

@app.route('/users', methods=['GET'])
def get_users():
    app.logger.info('get users')

    user_service = UserService()

    # pass off data to service

    users = user_service.get_users()

    app.logger.info('users={}'.format(users))

    return jsonify(to_dic_dto_list(users))
