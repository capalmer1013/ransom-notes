import uuid
import random

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, select
from sqlalchemy.sql import func
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import joinedload


db = SQLAlchemy()

class GAME_STATES:
    PREGAME = "pregame"
    AWAITING = "awaiting"
    SELECTION = "selection"

class BaseMixin(object):
    id = db.Column(db.Integer, primary_key=True, )
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
    __tablename__ = "game"
    state = db.Column(db.String, nullable=False, default=GAME_STATES.PREGAME)
    prompt_id = db.Column(db.Integer, db.ForeignKey("prompt.id"))
    players = db.relationship('Player', backref='game')

    @staticmethod
    def delete(id, **kw):
        game = Game.query.filter_by(id=id).first()
        game.deleteOne()
    
    @classmethod
    def getOne(cls, id):
        return cls.query.filter_by(id=id).options(joinedload(Game.players)).first()

class Player(BaseMixin, db.Model):
    __tablename__ = "player"
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"))
    response = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=False, default="NoName")
    ref_player_words = db.relationship(
        "Ref_Player_Words", back_populates="player", cascade="delete"
    )
    
    @classmethod
    def create(cls, **kw):
        player = cls(**kw)
        db.session.add(player)
        db.session.commit()
        for each in Word.getRandom():
            Ref_Player_Words.create(player_id=player.id, word_id=each.id)
        
        return player

    @staticmethod
    def delete(id, **kw):
        user = Player.query.filter_by(id=id).first()
        user.deleteOne()

class Word(BaseMixin, db.Model):
    __tablename__ = "word"
    text = db.Column(db.String, nullable=False)
    ref_player_words = db.relationship("Ref_Player_Words", back_populates="word", cascade="delete")

    @staticmethod
    def getRandom(n: int=20):
        return random.choices(Word.getAll(), k=n)

    @staticmethod
    def delete(id, **kw):
        user = Word.query.filter_by(id=id).first()
        user.deleteOne()

class Ref_Player_Words(db.Model):
    __tablename__ = "ref_player_word"
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('word.id'), primary_key=True)
    player = db.relationship("Player", back_populates="ref_player_words")
    word = db.relationship("Word", back_populates="ref_player_words")

    @staticmethod
    def getByPlayerID(id, **kw):
        return Ref_Player_Words.query.filter_by(player_id=id).options(joinedload(Ref_Player_Words))

    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()
        return obj

class Prompt(BaseMixin, db.Model):
    __tablename__ = "prompt"
    text = db.Column(db.String, nullable=True)
    
    @staticmethod
    def delete(id, **kw):
        user = Prompt.query.filter_by(id=id).first()
        user.deleteOne()