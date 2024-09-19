from flask import Blueprint, render_template, request, jsonify, redirect, url_for

# initialize the blueprint
views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Gagan")


# returning index
@views.route("/index")
def index():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)

@views.route("/profile")
def profile():
    return render_template("profile.html")

# returning json
@views.route("/json")
def get_json():
    return jsonify({'name': 'Gagan', 'coolness': 10})

# get data from a request(in json format)
# and redirect
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))
