from flask import Blueprint

from api.mongo_api.mongo_instances import instance_api

mongo_route = Blueprint('mongo_route', __name__)
mongo_route.register_blueprint(instance_api, url_prefix='/instances')
