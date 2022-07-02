#!/usr/bin/python3
"""
Review class module, inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class defines attributes/methods for Users:
    
    Public instance attributes:
    place_id (string): To contain the place id (from Place class) of which the review belongs, initialized with empty string
    user_id (string): To contain the user id (from User class) of the user that posted the review, initialized with empty string
    text (string): To contain the review text, initialized with empty string
    
    Magic method:
    __init__: Calls the __init__ method from parent with the super() method
    """
    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs):
        """
        Class instantation: uses init from parent class wit super
        """
        super().__init__(*args, **kwargs)
