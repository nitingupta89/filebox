from flask import render_template, redirect, url_for, request, session
from flask_dance.contrib.google import google
from app.middlewares.auth import login_required

from app import flask_app, db, google_bp, login_manager


# Listen for GET requests to /upload_file
@flask_app.route("/upload_file")
@login_required
def upload_file():
    # Show the upload_file HTML page:
    return render_template('file_upload.html')


@flask_app.route("/")
def home():
    return redirect(url_for("upload_file"))


@flask_app.route("/assets")
@login_required
def assets_page():
    # Show the assets HTML page:
    return render_template('assets.html')
