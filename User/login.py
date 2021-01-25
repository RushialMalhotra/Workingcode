from flask_restful import Resource
from flask import request, jsonify


class login(Resource) :
def auth():
     """function to login into vendor assessor assessment in which token expires in 4 days
            Args:
                user_name:
                password:
    """
    if request.method == 'POST':
        body = request.get_json()
        try:
            email = self.body['email']
            password = self.body['password']

            user_db = collection_user.find_one({"email": email})
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
            return bad_request(str(e))
    else:
        not_found()
