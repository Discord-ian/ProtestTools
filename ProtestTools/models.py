from flask_login import UserMixin
class Event:

    def __init__(self):
        self.name = None
        self.date = None
        self.time = None
        self.address = None
        self.city = None
        self.zip_code = None
        # TODO: Change how self.country works
        self.country = None

    def dict(self):
        return_dict = {"event_name": self.name, "date": self.date, "location": {}}
        return_dict["location"]["address"] = self.address
        return_dict["location"]["city"] = self.city
        return_dict["location"]["zip_code"] = self.zip_code
        return_dict["location"]["country"] = self.country
        return return_dict

class User(Uesr)