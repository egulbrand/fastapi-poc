import os 
import pymongo

DB_URL = os.environ['DB_URL']
DB_NAME = os.environ['DB_NAME']

class MongoManager:
    __instance = None
    @staticmethod
    def getInstance():
        if MongoManager.__instance == None:
            MongoManager()
        return MongoManager.__instance
    
    def __init__(self):
        if MongoManager.__instance == None:
            MongoManager.__instance = pymongo.MongoClient(DB_URL)

    @staticmethod
    def getDB():
        return MongoManager.__instance[DB_NAME]
    
    @staticmethod
    def closeDB():
        MongoManager.__instance.close()

