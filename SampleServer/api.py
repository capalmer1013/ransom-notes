from flask import Flask, jsonify, request, make_response
from flask_restx import Resource, Api, reqparse, fields

from .models import Game, Player, Word, Ref_Player_Words, Prompt

app = Flask(__name__)
api = Api(app, title="Sample REST api")

user_fields = api.model(
    "User", {"id": fields.Integer, "username": fields.String}
)

@api.route("/games")
class Games(Resource):
    # @api.doc(description="Get all Users")
    # @api.marshal_with(user_fields, as_list=True)
    def get(self):
        return [x.__dict__ for x in Game.getAll()]

    @api.doc(description="Create New Game")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("player_name", required=True, type=str)
        args = parser.parse_args()
        game = Game.create()
        player = Player.create()
        return {
            "game_id": game.id,
            "player_id": player.id
        }

@api.route("/games/<game_id>/players")
class Players(Resource):
    @api.doc(description="Create User in game (join game)")
    def post(self, game_id):
        parser = reqparse.RequestParser()
        parser.add_argument("player_name", required=True, type=str)
        args = parser.parse_args()
        player = Player.create(game_id=game_id)
        game = Game.getOne(game_id)
        return {
            "player_id": player.id,
            "game_state": game.state,
            "players": [x.id for x in game.players],
            "prompt": Prompt.getOne(game.prompt_id),
            "responses": [x.response for x in Player.query.filter_by(game_id=game_id)]
        }

@api.route("/games/<gameID>")
class Users(Resource):
    @api.doc(description="Get all Users")
    @api.marshal_with(user_fields, as_list=True)
    def get(self):
        return [x.__dict__ for x in Game.getAll()]

    @api.doc(description="Create User")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, type=str)
        args = parser.parse_args()
        Game.create(**args)
        return {}

@api.route("/games/<gameID>/cards")
class Users(Resource):
    @api.doc(description="Get all Users")
    @api.marshal_with(user_fields, as_list=True)
    def get(self):
        return [x.__dict__ for x in Game.getAll()]

    @api.doc(description="Create User")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, type=str)
        args = parser.parse_args()
        Game.create(**args)
        return {}

@api.route("/games/<gameID>/cards/winner")
class Users(Resource):
    @api.doc(description="Get all Users")
    @api.marshal_with(user_fields, as_list=True)
    def get(self):
        return [x.__dict__ for x in Game.getAll()]

    @api.doc(description="Create User")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, type=str)
        args = parser.parse_args()
        Game.create(**args)
        return {}