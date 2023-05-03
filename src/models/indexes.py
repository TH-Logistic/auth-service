from pymongo.database import Database


def createIndex(mongo_db: Database):
    mongo_db.users.create_index(('email'), unique=True)
    mongo_db.users.create_index(('phoneNumber'), unique=True)
