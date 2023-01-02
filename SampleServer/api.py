from flask import Flask, jsonify, request, make_response
from flask_restx import Resource, Api, reqparse, fields

from .models import User_Account

app = Flask(__name__)
api = Api(app, title="Sample REST api")

user_fields = api.model(
    "User", {"id": fields.Integer, "username": fields.String}
)

@api.route("/games")
class Users(Resource):
    @api.doc(description="Get all Users")
    @api.marshal_with(user_fields, as_list=True)
    def get(self):
        return [x.__dict__ for x in User_Account.getAll()]

    @api.doc(description="Create User")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, type=str)
        args = parser.parse_args()
        User_Account.create(**args)
        return {}

@api.route("/games/<gameID>/players")
class Users(Resource):
    @api.doc(description="Get all Users")
    @api.marshal_with(user_fields, as_list=True)
    def get(self):
        return [x.__dict__ for x in User_Account.getAll()]

    @api.doc(description="Create User")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, type=str)
        args = parser.parse_args()
        User_Account.create(**args)
        return {}

@api.route("/games/<gameID>")
class Users(Resource):
    @api.doc(description="Get all Users")
    @api.marshal_with(user_fields, as_list=True)
    def get(self):
        return [x.__dict__ for x in User_Account.getAll()]

    @api.doc(description="Create User")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, type=str)
        args = parser.parse_args()
        User_Account.create(**args)
        return {}

@api.route("/games/<gameID>/cards")
class Users(Resource):
    @api.doc(description="Get all Users")
    @api.marshal_with(user_fields, as_list=True)
    def get(self):
        return [x.__dict__ for x in User_Account.getAll()]

    @api.doc(description="Create User")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, type=str)
        args = parser.parse_args()
        User_Account.create(**args)
        return {}

@api.route("/games/<gameID>/cards/winner")
class Users(Resource):
    @api.doc(description="Get all Users")
    @api.marshal_with(user_fields, as_list=True)
    def get(self):
        return [x.__dict__ for x in User_Account.getAll()]

    @api.doc(description="Create User")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, type=str)
        args = parser.parse_args()
        User_Account.create(**args)
        return {}