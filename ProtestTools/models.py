from flask_login import UserMixin
from app import client


class Event:

    def __init__(self):
        self.name = None
        self.date = None
        self.time = None
        self.address = None
        self.cause = None
        self.description = None
        self.city = None
        self.zip_code = None
        # TODO: Change how self.country works
        self.country = None
        self.lat = None
        self.lng = None
        self.id = None

    def dict(self):
        return_dict = {
            "event_name": self.name,
            "cause": self.cause,
            "description": self.description,
            "date": self.date,
            "time": self.time,
            "location": {},
        }
        return_dict["location"]["address"] = self.address
        return_dict["location"]["city"] = self.city
        return_dict["location"]["zip_code"] = self.zip_code
        return_dict["location"]["lat"] = self.lat
        return_dict["location"]["lng"] = self.lng
        return return_dict


class User(UserMixin):
    def __init__(self, username, id, active=True):
        self.id = id
        self.username = username
        self.active = active
