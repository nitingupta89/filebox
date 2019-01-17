from flask import render_template

from app import flask_app


# Listen for GET requests to /upload_file
@flask_app.route("/upload_file")
def account():
  # Show the upload_file HTML page:
  return render_template('file_upload.html')
