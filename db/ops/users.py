from db.mongo_manager import MongoManager

def getAllUsers():
    users = MongoManager.getDB()["users"].find()
    return users

def getUser(id):
    user = None
    user_query = {"_id": id}
    user = MongoManager.getDB()["users"].find_one(user_query)
    # user = self._app.database["users"].find_one(user_query)
    return user

def getUserByUserName(username):
    user = None
    user_query = {"username": username}
    user = MongoManager.getDB()["users"].find_one(user_query)
    # user = self._app.database["users"].find_one(user_query)
    print(str(user))
    print(type(user))
    return user
