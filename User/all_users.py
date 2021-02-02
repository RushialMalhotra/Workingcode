from flask import request, jsonify
from flask_restful import Resource
from User.register import json_response, bad_request
        
class All_users(Resource):

    def __init__(self, **kwargs):
        self.collection_user = kwargs['collection_user']
        
    def get(self, **kwargs):
        try:
            users = self.collection_user.find({})
            return json_response('All users fetched successfully',200, {'Users': [user for user in users]})
        except Exception as e:  
            return json_response('Method not allowed',400)