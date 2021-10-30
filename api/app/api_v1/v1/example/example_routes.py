# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Routes Example
#########################################################

from flask import request, jsonify
from app.api_v1 import api
from app.controllers import ExampleController as Controller


@api.route('/index', methods=['GET'])
def get_index():
    response = Controller.get_index()
    return jsonify(data=response)

@api.route('/request', methods=['GET'])
def get_query():
    response = Controller.request_query()
    return jsonify(data=response)

@api.route('/save', methods=['POST'])
def save_query():
    response = Controller.save_query()
    return jsonify(data=response)

@api.route('/update', methods=['POST'])
def update_query():
    response = Controller.update_query()
    return jsonify(data=response)

@api.route('/delete', methods=['DELETE'])
def delete_query():
    response = Controller.delete_query()
    return jsonify(data=response)


