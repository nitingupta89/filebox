from .views.health_check import HealthCheckView
from app.blueprint import api


# Add resources
api.add_resource(HealthCheckView, '/filebox/health_check')
