# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Controller Example
#########################################################

from app.exception import InternalServerError
from app.models import ExampleModel
from app import db


class ExampleController:

    @staticmethod
    def get_index():
        try:
            response = {
                'ok': True,
                'message': 'Response OK, method get_index'
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    def request_query():
        try:
            query = ExampleModel.export_data()
            response = {
                'ok': True,
                'message': 'Response OK, method request_query',
                'Query' : query
            }
            return query
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)
            
    def save_query():
        try:
            query = ExampleModel.save()
            response = {
                'ok': True,
                'message': 'Response OK, method save_query',
                'Query' : query
            }
            return query
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    def update_query():
        try:
            query = ExampleModel.update()
            response = {
                'ok': True,
                'message': 'Response OK, method update_query',
                'Query' : query
            }
            return query
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    def delete_query():
        try:
            query = ExampleModel.delete()
            response = {
                'ok': True,
                'message': 'Response OK, method delete_query',
                'Query' : query
            }
            return query
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)
    
    
    
