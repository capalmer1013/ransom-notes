import uuid

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from sqlalchemy.sql import func
from sqlalchemy.dialects import postgresql

db = SQLAlchemy()

class GAME_STATES:
    PREGAME = "pregame"
    AWAITING = "awaiting"
    SELECTION = "selection"

class BaseMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        db.DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
    # Makes sure the columns are added to the end of the table
    created_at._creation_order = 9998
    updated_at._creation_order = 9999

    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def deleteOne(cls, **kw):
        obj = cls.query.filter_by(**kw).first()
        if obj:
            db.session.delete(obj)
            db.session.commit()
    
    @classmethod
    def getOne(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def getAll(cls):
        return cls.query.all()

class Game(BaseMixin, db.Model):
    __tablename__ = "games"
    state = db.Column(db.String, nullable=False, default=GAME_STATES.PREGAME)
    prompt_id = db.Column(db.Integer, db.ForeignKey("prompt.id"))
    
    @staticmethod
    def delete(id, **kw):
        game = Game.query.filter_by(id=id).first()
        game.deleteOne()

class Player(BaseMixin, db.Model):
    __tablename__ = "players"
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"))
    response = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=False, default="NoName")
    
    @staticmethod
    def delete(id, **kw):
        user = Player.query.filter_by(id=id).first()
        user.deleteOne()

class Word(BaseMixin, db.Model):
    __tablename__ = "words"
    text = db.Column(db.String, nullable=False)

    @staticmethod
    def delete(id, **kw):
        user = Word.query.filter_by(id=id).first()
        user.deleteOne()

ref_player_words = db.Table('ref_player_words',
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'), primary_key=True),
    db.Column('word_id', db.Integer, db.ForeignKey('word.id'), primary_key=True)
)

class Prompt(BaseMixin, db.Model):
    __tablename__ = "prompts"
    text = db.Column(db.String, nullable=True)
    
    @staticmethod
    def delete(id, **kw):
        user = Prompt.query.filter_by(id=id).first()
        user.deleteOne()