from flask import request


def hello_world():
    return {"hello": "World!"}


def help():
    return {"welcome":"Welcome to my API"}


def salute():
    name = request.args.get("name")
    return {"message": f"Hello, {name}!"}