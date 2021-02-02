from flask import request, jsonify
from flask_restful import Resource
from User.register import json_response, bad_request
from flask_jwt_extended import (JWTManager, create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, set_access_cookies,
                                set_refresh_cookies)


class Posts(Resource):
        
    def __init__(self, **kwargs):
            self.collection_posts = kwargs['collection_posts']
        
    def post(self, *args, **kwargs):
        try:
            _json = request.get_json()
            content = _json['content'] 
            title = _json['title'] 
        
            current_user = get_jwt_identity()
            if not content or not title:
                return json_response('Keys missing',400)
            if self.collection_posts.insert_one({"content": content, 'title': title, 'posted_by': current_user}):
                return json_response('Post added successfully', 200)
        except:
             return json_response('Method not allowed',400)

                
    def get(self, **kwargs):
        try:
            posts = self.collection_posts.find({},projection={"_id": False})
            return json_response('Post fetched successfully',200, {'posts': [post for post in posts]})
        except Exception as e:  
            return json_response('Method not allowed',400)