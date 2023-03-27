import os

from flask import Blueprint, jsonify

from module.mongo.mongo_instance import MongoInstance

instance_api = Blueprint('instances', __name__)

mogo_instance_map = {}

# Get all Mogo instances
# eg: PD_MOGO_DEFAULT_HOST=localhost
#     PD_MOGO_DEFAULT_PORT=27017
prefix_len = len('PD_MONGO_')
env_map = {k[prefix_len:]: v for k, v in os.environ.items() if k.startswith('PD_MONGO_')}
for key, value in env_map.items():
    index = key.index('_')
    name = key[:index].lower()
    conf_property = key[index + 1:]
    if name not in mogo_instance_map:
        mogo_instance_map[name] = MongoInstance(name.lower())
    mogo_instance = mogo_instance_map[name]
    if conf_property == 'HOST':
        mogo_instance.host = value
    elif conf_property == 'PORT':
        mogo_instance.port = value


@instance_api.route('', methods=['GET'])
def get_instance_list():
    return jsonify(list(mogo_instance_map.values()))
