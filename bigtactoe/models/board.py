from .base import db
from .base import ma

from marshmallow import fields

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contents = db.Column(db.String(81), nullable=False)

class BoardSchema(ma.Schema):
    id = fields.Integer()
    contents = fields.String()

board_schema = BoardSchema()
boards_schema = BoardSchema(many=True)
