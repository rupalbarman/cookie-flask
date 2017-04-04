import json
from flask import (Blueprint, request, url_for, redirect,
                    make_response, render_template, flash)


page = Blueprint("page", __name__, template_folder="templates")


__author__ = ["mmarconm", "Marcelo Marcon"]
__version__ = "1.0.0"


def get_cookie():
    try:
        data = json.loads(request.cookies.get("name"))
    except TypeError:
        data = {}
    return data


@page.route("/")
def index():
    return render_template("index.html", saves=get_cookie())


@page.route("/save", methods=["POST"])
def save():
    flash("Works Pretty Well")
    response = make_response(redirect(url_for("page.index")))
    data = get_cookie()

    data.update(dict(request.form.items()))
    response.set_cookie("name", json.dumps(data))
    return response
