import json


class Config:
    def __init__(self):
        config = open("./config.json", "r")
        config = json.load(config)

        self.name = config["Name"]

        self.token = config["Bot"]["Token"]
        self.description = config["Bot"]["Description"]
        self.activity = config["Bot"]["Activity"]
        self.status = config["Bot"]["Status"]

        self.database = config["Database"]["Name"]
        self.uri = config["Database"]["URI"]

        self.guild = config["Ids"]["Guild"]

        self.save = config["Save"]