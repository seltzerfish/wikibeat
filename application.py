#!/usr/bin/env python
import wikipedia
import bottle
from bottle import template, static_file, redirect, request, get, post, route
from beaker.middleware import SessionMiddleware
from random import choice
from record import record_rap
from time import sleep

session_opts = {
    "session.cookie_expires": 3600 * 24,
    "session.encrypt_key": "TEST KEY PLEASE IGNORE",
    "session.httponly": True,
    "session.timeout": 3600 * 24,  # 1 day
    "session.type": "memory",
    "session.validate_key": True,
    "session.auto": True,
}
app = SessionMiddleware(bottle.app(), session_opts)


###############################################################################
# Session Functions ###########################################################
###############################################################################


def get_session():
    return bottle.request.environ.get("beaker.session")


###############################################################################
# Routes ######################################################################
###############################################################################


@route("/", name="index")
def index():
    s = bottle.request.environ.get("beaker.session")
    return template("index", sess=get_session())


@route("/submit_topic", method="POST")
def accept_input():
    if request.method == "POST":
        inp = request.forms.get("inp")
        try:
            page = wikipedia.page(inp)
        except Exception:
            options = wikipedia.search(inp)[:5]
            redirect("/choose/" + str(options))
        r = record_rap(page.url)
        if not r:
            redirect("/sorry")
        return "done"

    else:
        return template("index", sess=get_session())
    return inp


@route("/choose/<options>")
def choose(options):
    options = eval(options)
    return template("choose", sess=get_session(), options=options)


@route("/chosen/<choice>")
def chosen(choice):
    page = wikipedia.page(choice)
    r = record_rap(page.url)
    if not r:
        redirect("/sorry")
    return "done"


@route("/sorry")
def sorry():
    return template("sorry")


@route("/static/<file:path>")
def send_static(file):
    return static_file(file, root="static/")


if __name__ == "__main__":
    bottle.run(app=app, host="localhost", port=8080, reloader=True, debug=True)
