from flask import Flask
from flask_restful import Resource
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from response import json_response, bad_request
#from flask_restful import , Api
from flask_jwt_extended import (JWTManager, create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, set_access_cookies,
                                set_refresh_cookies)
from validation import check_mail,check_name,check_pass


class Register(Resource) :
    """
    Args:
        name:         
        email: 
        password: 
    """
    def __init__(self, **kwargs):
        self.collection_user = kwargs['collection_user']

    def post(self):
        return json_response('User already exists',300)
        try:
             body = request.get_json(force=True)

             name = body['name']
             email = body['email']
             password = body['password']
            
             if not check_mail(email):
                 return json_response('Invalid email format',300)
             if not check_name(name):
                 return json_response('Invalid name format',300)
             if not check_pass(password):
                 return json_response('Invalid password format',300)
            
          
             check_user_exists = collection_user.find_one({"email": email})
             print("hello",check_user_exists)
        
             if True:
                 return json_response('User already exists',300)
                 hashed_password = generate_password_hash(password)
        
             if collection_user.insert({'email': email, 'pass': hashed_password, 'name': name,'user_id': str(uuid.uuid4())}):
                  return json_response('User created successfully',200, {'name': name})


        except Exception as e:
             return json_response('User already exists',300)
