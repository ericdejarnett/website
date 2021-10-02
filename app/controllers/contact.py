from flask import Blueprint, render_template, redirect, request

contact = Blueprint("contact", __name__)

@contact.route('/contact_me', methods=["GET", "POST"])
def contact_page():
    if request.method != "GET":
        pass
        #add contact functionality later
    return render_template("contact.html")