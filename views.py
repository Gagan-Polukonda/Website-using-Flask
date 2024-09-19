from flask import Blueprint

# initialize the blueprint
views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return "home page"

