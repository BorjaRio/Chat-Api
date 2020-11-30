from api.app import app
from flask import request
from helpers.mongoConnection import get_mydatabase, insert_user , insert_chat ,insert_message
from bson import json_util


# Decorators


@app.route("/mydatabase")
def data():
    user= request.args.get("user")
    return get_mydatabase(user)

## insertar usuario

@app.route("/user/create/<username>")
def insert_u(username):
    return json_util.dumps(insert_user(dict(request.args)))

#insertar chat

@app.route("/chat/create/<chatname>/<user_id>")
def insert_ch(chatname,user_id):
    print(chatname, user_id)
    return json_util.dumps(insert_chat({"chatname":chatname,"usuarios":user_id}))

@app.route("/chat/create/<chatname>")
def insert_cha(chatname):
    integrantes = request.args.getlist("user_id")
    print({"nombre chat":chatname, "Lista integrantes":integrantes})
    result = {"nombre chat":chatname, "Lista integrantes":integrantes}
    return json_util.dumps(insert_chat(result))

#insertar mensaje

@app.route("/messages/create/<chat_id>/<user_id>/<text>")
def insert_mess(chat_id, user_id, text):
    return json_util.dumps(insert_message(chat_id, user_id, dict(request.args)))