from flask import Blueprint, render_template
from app.utils.db_utils import get_db_connection

homepage = Blueprint("homepage", __name__)

@homepage.route('/', methods=["GET"])
def index():
    return render_template("index.html")