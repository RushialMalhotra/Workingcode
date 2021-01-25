from flask import Flask
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from response import json_response, bad_request
from flask_restful import Api
from flask_jwt_extended import (JWTManager, create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, set_access_cookies,
                                set_refresh_cookies)
import uuid

from validation import check_mail,check_name,check_pass
from register import Register
 
app = Flask(__name__)
api = Api(app)




app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
app.config['JWT_COOKIE_CSRF_PROTECT']= False
app.config['JWT_SECRET_KEY']  = 'jwt-supersecret'
jwt = JWTManager(app)
app.secret_key = "secretkey"
cluster = MongoClient("mongodb://localhost:27017/Users")
db = cluster['Users']
collection_user = db['users']
collection_posts = db['posts']


# @app.route('/register', methods=['POST'])

api.add_resource(Register, "/register", resource_class_kwargs={'collection_user': collection_user})


# @app.route('/login', methods=['POST'])
# def login():
#     if request.method == 'POST':
#         body = request.get_json()
#         try:
#             email = body['email']
#             password = body['password']

#             user_db = collection_user.find_one({"email": email})
#             if not user_db:
#                 return json_response('User does not exists',300)
            
#             if check_password_hash(user_db['pass'],password):
#                 access_token = create_access_token(
#                         identity=user_db['name'])
                    
#                 response = jsonify({'Login': True})
#                 set_access_cookies(response, access_token)
#                 return response, 200

#             else:
#                 return json_response('Password does not match', 400)


#         except Exception as e:
#             return bad_request(str(e))
#     else:
#         not_found()


# @app.route('/post', methods=['POST','GET'])
# @jwt_required
# def post():
#     try:
        
    
#         if request.method == 'POST':
#             _json = request.get_json()
#             content = _json['content'] 
#             title = _json['title'] 
#             current_user = get_jwt_identity()
            
#             if not content or not title:
#                 return json_response('Keys missing',400)
#             if collection_posts.insert_one({"content": content, 'title': title, 'posted_by': current_user}):
#                 return json_response('Post added successfully', 200)

#         if request.method == 'GET':
#             posts = collection_posts.find({},projection={"_id": False})
#             return json_response('Post fetched successfully',200, {'posts': [post for post in posts]})
#         else: 
#             return json_response('Method not allowed',400)
    
#     except Exception as e:  
#             return bad_request(str(e))
    

# @app.errorhandler(404)
# def not_found(error=None):
#     message = {
#         'status':404,
#         'message':'Not found' + request.url
#     }
#     resp = jsonify(message)

#     resp.status_code = 404

#     return resp

if __name__ == "__main__":
    app.run(debug=True)
