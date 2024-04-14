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
        self.state = None
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
        return_dict["location"]["state"] = self.state
        return_dict["location"]["zip_code"] = self.zip_code
        return_dict["location"]["lat"] = self.lat
        return_dict["location"]["lng"] = self.lng
        return return_dict


def neat_address(event):
    address = "{0.address}\n{0.city}, {0.state} {0.zip_code}".format(event.location)


class User(UserMixin):
    def __init__(self, username, id, active=True):
        self.id = id
        self.username = username
        self.active = active
