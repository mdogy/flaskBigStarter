# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>

from flask_user import UserMixin
from flask_user.forms import RegisterForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from app import db

class ToDo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(255),
                     nullable=False,
                     server_default=u'')
    description = db.Column(db.UnicodeText(),
                     nullable=False,
                     server_default=u'')
    created_at = db.Column(db.DateTime(),
                     server_default=db.func.now())
    updated_at = db.Column(db.DateTime(),
                     server_default=db.func.now(),
                     server_onupdate=db.func.now())
    due_at =  db.Column(db.DateTime())
    completed = db.Column(db.Boolean(),
                          nullable=False,
                          server_default='0')
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
