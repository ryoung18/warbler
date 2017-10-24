from flask import Blueprint, make_response, jsonify
from flask_restful import Api, Resource
from project.users.models import User
from project import db

user_blueprint = Blueprint('users', __name__)
users_api = Api(user_blueprint)

# @users_api.resource('/')
class Users(Resource):
    def get(self): #get all users
        # call database using user_id
        # send JSON response with user object
        return make_response(jsonify({ "test": "one" }))
    def post(self): #create new user
        # parse JSON body
        # call database to create user
        # send JSON response of created user
        pass

class User(Resource):
    def get(self, user_id): # get single user
        # call database using user_id
        # send JSON response with user object
        
        # return make_response(jsonify({ "test": "one" }))
        pass
    def delete(self, user_id): #delete user
        pass



users_api.add_resource(Users)
users_api.add_resource(User, '/<string:user_id>')

