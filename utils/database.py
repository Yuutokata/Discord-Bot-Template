import pymongo
from utils.config import Config

config = Config()

cluster = pymongo.MongoClient(config.uri)

database = cluster[str(config.database)]
