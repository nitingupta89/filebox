from .views.health_check import HealthCheckView
from .views.s3 import S3View
from .views.google_login import GoogleLoginView
from .views.assets import AssetsView

from app.blueprint import api


# Adding resources
api.add_resource(HealthCheckView, '/health_check')
api.add_resource(S3View, '/get_signed_url')
api.add_resource(GoogleLoginView, '/gCallback')
api.add_resource(AssetsView, '/assets')
