import json


class Config:
    def __init__(self):
        config = open("./config.json", "r")
        config = json.load(config)

        self.name = config["name"]

        self.token = config["bot"]["token"]
        self.description = config["bot"]["description"]

        self.activity_status = config["bot"]["activity"]["status"]
        self.activity_text = config["bot"]["activity"]["text"]

        self.status = config["bot"]["status"]

        self.database = config["database"]["name"]
        self.uri = config["database"]["uri"]

        self.guild = config["ids"]["guild"]

        self.color = config["design"]["color"]
        self.footer_text = config["design"]["footer"]
        self.footer_icon = config["design"]["icon_url"]
        self.image = config["design"]["image"]
        self.thumbnail = config["design"]["thumbnail"]

        self.save = config["save"]
