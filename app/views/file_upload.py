from flask import render_template, redirect, url_for, request
from flask_dance.contrib.google import google
from flask_login import (
    LoginManager,
    current_user,
    login_user,
    logout_user
)
from flask_dance.consumer.backend.sqla import SQLAlchemyBackend
from flask_dance.consumer import oauth_authorized
from sqlalchemy.orm.exc import NoResultFound
from app.models.user import OAuth, User
from flask import flash

from app import flask_app, db, google_bp


# Listen for GET requests to /upload_file
@flask_app.route("/upload_file")
def upload_file():
    if not google.authorized:
        return redirect(url_for("google.login"))

    # Show the upload_file HTML page:
    return render_template('file_upload.html')


@flask_app.route("/login/google/authorized")
def g_authorized():
    return redirect(url_for("upload_file"))


# create/login local user on successful OAuth login
@oauth_authorized.connect
def google_logged_in(blueprint, token):
    import pdb; pdb.set_trace()
    if not token:
        flash("Failed to log in with Google.", category="error")
        return False

    resp = blueprint.session.get("/oauth2/v2/userinfo")
    if not resp.ok:
        msg = "Failed to fetch user info from Google."
        flash(msg, category="error")
        return False

    google_info = resp.json()
    google_user_id = str(google_info["id"])

    # Find this OAuth token in the database, or create it
    query = OAuth.query.filter_by(
        provider=blueprint.name,
        provider_user_id=google_user_id,
    )
    try:
        oauth = query.one()
    except NoResultFound:
        oauth = OAuth(
            provider=blueprint.name,
            provider_user_id=google_user_id,
            token=token,
        )

    if oauth.user:
        # If this OAuth token already has an associated local account,
        # log in that local user account.
        # Note that if we just created this OAuth token, then it can't
        # have an associated local account yet.
        login_user(oauth.user)
        flash("Successfully signed in with GitHub.")

    else:
        # If this OAuth token doesn't have an associated local account,
        # create a new local user account for this user. We can log
        # in that account as well, while we're at it.
        user = User(
            # Remember that `email` can be None, if the user declines
            # to publish their email address on GitHub!
            email=google_info["email"],
            name=google_info["name"],
        )
        # Associate the new local user account with the OAuth token
        oauth.user = user
        # Save and commit our database models
        db.session.add_all([user, oauth])
        db.session.commit()
        # Log in the new local user account
        login_user(user)
        flash("Successfully signed in with GitHub.")

    # Since we're manually creating the OAuth model in the database,
    # we should return False so that Flask-Dance knows that
    # it doesn't have to do it. If we don't return False, the OAuth token
    # could be saved twice, or Flask-Dance could throw an error when
    # trying to incorrectly save it for us.
    return False


@flask_app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("google.login"))
