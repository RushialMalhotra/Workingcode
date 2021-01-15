@app.route('/post', methods=['POST','GET'])
@jwt_required
def post():
    try:
        
    
        if request.method == 'POST':
            _json = request.get_json()
            content = _json['content'] 
            title = _json['title'] 
            current_user = get_jwt_identity()
            
            if not content or not title:
                return json_response('Keys missing',400)
            if collection_posts.insert_one({"content": content, 'title': title, 'posted_by': current_user}):
                return json_response('Post added successfully', 200)

        if request.method == 'GET':
            posts = collection_posts.find({},projection={"_id": False})
            return json_response('Post fetched successfully',200, {'posts': [post for post in posts]})
        else: 
            return json_response('Method not allowed',400)
    
    except Exception as e:  
            return bad_request(str(e))