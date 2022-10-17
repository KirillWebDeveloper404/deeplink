from enum import unique
from .BaseModel import BaseModel
from peewee import *


class User(BaseModel):
    tg_id = TextField()
    name = CharField(max_length=100, unique=False)
    phone = CharField(max_length=20, unique=True)

    class Meta:
        table_name = 'panel_user'
