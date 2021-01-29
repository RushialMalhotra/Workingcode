from flask import request, jsonify
from flask_restful import Resource
from User.register import json_response, bad_request
        
class All_users(Resource):

    def __init__(self, **kwargs):
        self.collection_user = kwargs['collection_user']
        
    def get(self, collection_user):
        try:
            posts = collection_user.find({},projection={"_id": False})
            return json_response('All users fetched successfully',200, {'posts': [post for post in posts]})
        except Exception as e:  
            return json_response('Method not allowed',400)