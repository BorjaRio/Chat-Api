from pymongo import MongoClient

client = MongoClient()

db = client.get_database("mydatabase")

def get_mydatabase(name):
    curs = db.mydatabase.find({"name":name})
    return list(curs)

#funcion user name
def insert_user(username):
    curs = db.user.insert_one(username)
    return {"_id":curs.inserted_id}
#funcion chatname
def insert_chat(chatname):
    curs=db.chat.insert_one(chatname)
    return {"_id": curs.inserted_id}

#funcion message

def insert_message(chat_id, user_id, text):
    curs=db.message.insert_one({"message":text, "chat_id": chat_id, "user_id":user_id})
    return {"_id": curs.inserted_id}