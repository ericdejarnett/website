from flask import Blueprint, render_template

homepage = Blueprint("homepage", __name__)

@homepage.route('/', methods=["GET"])
def index():
    return render_template("index.html")