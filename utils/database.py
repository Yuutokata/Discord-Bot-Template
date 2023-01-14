import pymongo
from utils.config import Config

config = Config()

database = pymongo.MongoClient(config.uri)

points = database[str(config.database)]
