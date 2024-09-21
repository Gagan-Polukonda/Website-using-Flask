from flask import Blueprint, render_template, request, jsonify, redirect, url_for

# initialize the blueprint
views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Gagan")


# returning index
@views.route("/username")
def index():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)


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


@views.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("views.user", usr=user))
    else:
        return render_template("profile.html")


@views.route("/<usr>")
def user(usr):
    if usr in ['Gagan']:
        return f"<h1>{usr}</h1>"
    else:
        return "<h1>User not found</h1>"