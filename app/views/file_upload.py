from flask import Flask, render_template, request, redirect, url_for
import os, json, boto3

from app import flask_app


# Listen for GET requests to /upload_file
@flask_app.route("/upload_file")
def account():
  # Show the upload_file HTML page:
  return render_template('file_upload.html')
