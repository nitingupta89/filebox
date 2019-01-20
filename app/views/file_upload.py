from flask import render_template, redirect, url_for, request, session
from flask_dance.contrib.google import google

from app import flask_app, db, google_bp, login_manager


# Listen for GET requests to /upload_file
@flask_app.route("/upload_file")
def upload_file():
    if not google.authorized:
        return redirect(url_for("google.login"))

    # Show the upload_file HTML page:
    return render_template('file_upload.html')


@flask_app.route("/")
def home():
    return redirect(url_for("upload_file"))


@flask_app.route("/assets")
def assets_page():
    if not google.authorized:
        return redirect(url_for("google.login"))

    # Show the upload_file HTML page:
    return render_template('assets.html')
