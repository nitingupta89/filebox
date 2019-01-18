import flask
import json
import flask_restful as restful

# from app import googlelogin
from app.models.user import User


class GoogleLoginView(restful.Resource):

    # method_decorators = [googlelogin.oauth2callback]

    def post(self, token, userinfo, **params):
        import pdb; pdb.set_trace()
        user = User.filter_by(google_id=userinfo['id']).first()
        if user:
            user.name = userinfo['name']
            user.avatar = userinfo['picture']
        else:
            user = User(google_id=userinfo['id'],
                        name=userinfo['name'],
                        avatar=userinfo['picture'])
        db.session.add(user)
        db.session.flush()
        login_user(user)
        return redirect(url_for('index'))
