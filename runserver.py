from werkzeug.serving import run_simple

from app import flask_app


if __name__ == '__main__':
    # Run Server
    run_simple(
        '0.0.0.0', 5000, flask_app, use_reloader=True,
        use_debugger=True, use_evalex=True
    )
