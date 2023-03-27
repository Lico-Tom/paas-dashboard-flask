import os

from flask import Blueprint, jsonify

from module.mongo.mongo_instance import MongoInstance

instance_api = Blueprint('instances', __name__)

mongo_instance_map = {}

# Get all Mongo instances
# eg: PD_MONGO_DEFAULT_HOST=localhost
#     PD_MONGO_DEFAULT_PORT=27017
prefix_len = len('PD_MONGO_')
env_map = {k[prefix_len:]: v for k, v in os.environ.items() if k.startswith('PD_MONGO_')}
for key, value in env_map.items():
    index = key.index('_')
    name = key[:index].lower()
    conf_property = key[index + 1:]
    if name not in mongo_instance_map:
        mongo_instance_map[name] = MongoInstance(name.lower())
    mongo_instance = mongo_instance_map[name]
    if conf_property == 'HOST':
        mongo_instance.host = value
    elif conf_property == 'PORT':
        mongo_instance.port = value


@instance_api.route('', methods=['GET'])
def get_instance_list():
    return jsonify(list(mongo_instance_map.values()))
