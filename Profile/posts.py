from flask import request, jsonify
from flask_restful import Resource
from User.register import json_response, bad_request


class Posts(Resource):
        
    def __init__(self, **kwargs):
            self.collection_user = kwargs['collection_user']
        
    def post(self, *args, **kwargs):
        try:
            _json = request.get_json()
            content = _json['content'] 
            title = _json['title'] 
        
            current_user = get_jwt_identity()
            if not content or not title:
                return json_response('Keys missing',400)
            if collection_posts.insert_one({"content": content, 'title': title, 'posted_by': current_user}):
                return json_response('Post added successfully', 200)
        except:
             return json_response('Method not allowed',400)

                
    def get(self, collection_posts):
        try:
            posts = collection_posts.find({},projection={"_id": False})
            return json_response('Post fetched successfully',200, {'posts': [post for post in posts]})
        except Exception as e:  
            return json_response('Method not allowed',400)