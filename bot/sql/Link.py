from enum import unique
from .BaseModel import BaseModel
from .User import User
from peewee import *


class Link(BaseModel):
    user = ForeignKeyField(model=User)
    name = CharField(max_length=1000)
    ozon = CharField(max_length=1000, unique=False, null=True)
    wb = CharField(max_length=1000, unique=False, null=True)
    ali = CharField(max_length=1000, unique=False, null=True)
    ym = CharField(max_length=1000, unique=False, null=True)

    class Meta:
        table_name = 'panel_link'
