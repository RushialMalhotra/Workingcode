from flask import request, jsonify
from flask_restful import Resource
from User.register import json_response, bad_request
        
class All_users(Resource):

    def __init__(self, **kwargs):
        self.collection_user = kwargs['collection_user']
        
    def get():
        

        try:
            all_users = collection_users.find({},projection={"_id": False})
            return json_response('All users fetched successfully',200, {'all_users': [all_users for users in users]}
        except Exception as e:  
            return bad_request(str(e))