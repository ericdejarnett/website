import time
from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.utils.db_utils import new_contact_entry

contact = Blueprint("contact", __name__)

@contact.route('/contact_me', methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        pass
        email = request.form['email']
        message = request.form['message']
        if not email:
            flash('Email is required!')
        elif not message:
            flash('You forgot to write anything!')
        else:
            new_contact_entry(email, message)
            flash('Your message has been sent!')
            time.sleep(5)
            return redirect(url_for('homepage.index'))
            
    return render_template("contact.html")