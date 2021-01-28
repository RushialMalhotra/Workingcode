from flask_restful import Resource
from flask import request, jsonify
from Authorization.response import json_response , bad_request


class Login(Resource) :
    
        def __init__(self, **kwargs):
            self.collection_user = kwargs['collection_user']
   
        def post(self, *args, **kwargs):
            
            body = request.get_json()
            
            try:
                email = body['email']
                password = body['password']

                user_db = collection.find_one({"email": email})
                if not user_db:
                    return json_response('User does not exists',300)
            
                if check_password_hash(user_db['pass'],password):
                    access_token = create_access_token(
                        identity=user_db['name'])
                    
                    response = jsonify({'Login': True})
                    set_access_cookies(response, access_token)
                    return response, 200

                else:
                    return json_response('Password does not match', 400)


            except Exception as e:
                return json_response('Please enter valid credentials', 300)
