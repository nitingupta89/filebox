from .views.health_check import HealthCheckView
from .views.s3 import S3View

from app.blueprint import api


# Add resources
api.add_resource(HealthCheckView, '/health_check')
api.add_resource(S3View, '/get_signed_url')
