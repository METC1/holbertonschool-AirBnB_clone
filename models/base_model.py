#!/usr/bin/python3
"""
BaseModel class module
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines all common attributes/methods for other classes

    Public attributes:
    id: string, assign an uuid (random uuid4()) when an instance is created
    created_at: datetime, assign current datetime when an instance is created
    updated_at: datetime, assign current datetime when an instance is created
    and it will be updated with every modification using the save(self) method

    Magic method:
    __str__: string representation of an instance of a class.
    Format: [<class name>] (<self.id>) <self.__dict__>

    Public instance methods:
    save: updates the attribute "updated_at" with the current datetime
    to_dict: returns a dictionary containing all keys/values of __dict__ of the
    instance and tha class name.

    """
    def __init__(self):
        """
        Class instantiation, assigns an id, creation and first update date/time
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Prints class instance. Format [self.Class name](self.id){self.dict}
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute of the instance
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Creates a dictionary version of the instance attributes
        """
        attributes_dict = vars(self).copy()
        # Add __class__ variable to attributes_dict
        attributes_dict["__class__"] = self.__class__.__name__
        # Convert created_at and updated_at to string object in ISO format
        attributes_dict["created_at"] = self.created_at.isoformat()
        attributes_dict["updated_at"] = self.updated_at.isoformat()

        return attributes_dict
