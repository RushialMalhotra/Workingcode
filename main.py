from flask import Flask
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from Authorization.response import json_response, bad_request
from Authorization.validation import check_mail, check_name, check_pass
from User.login import Login
from User.all_users import All_users
from Profile.posts import Posts
from User.register import Register
from flask_restful import Api
from flask_jwt_extended import (JWTManager, create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, set_access_cookies,
                                set_refresh_cookies)
import uuid
from Authorization.validation import check_mail,check_name,check_pass

 
app = Flask(__name__)
api_helper = Api(app)

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


api_helper.add_resource(Register, "/register", resource_class_kwargs={'collection_user': collection_user})

api_helper.add_resource(Login, "/login", resource_class_kwargs={'collection_user': collection_user})

api_helper.add_resource(Posts, "/post", resource_class_kwargs={'collection_user': collection_posts})

api_helper.add_resource(All_users, "/user", resource_class_kwargs={'collection_user': collection_user})




@app.errorhandler(404)
def not_found(error=None):
     message = {
         'status':404,
         'message':'Not found' + request.url
     }
     resp = jsonify(message)

     resp.status_code = 404

     return resp

if __name__ == "__main__":
    app.run(debug=True)
