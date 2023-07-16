#!/usr/bin/python3
"""user class, subclass of BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    '''representation of a customer'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
