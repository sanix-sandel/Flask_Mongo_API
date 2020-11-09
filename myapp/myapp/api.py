from flask import jsonify, request, make_response
from .models import *
from myapp import app
from bson import ObjectId

@app.route('/', methods=['GET'])
def home():
    return '<h1>Salut</h1>'


@app.route('/api/posts/create', methods=['POST'])
def create_post():
    post=Post.from_json(request.json)
    post.save()
    return make_response("Post created ", 200)



@app.route('/api/posts')
def get_posts():
    posts=Post.objects.all()
    return jsonify({'posts':[post.to_json() for post in posts]})


@app.route('/api/posts/<string:id>')
def get_post(id):
    post=Post.objects(id=id)
    return jsonify({'post':post.to_json()})


@app.route('/api/posts/update/<id>', methods=['UPDATE'])
def update_post(id):
    post=Post.objects(id=ObjectId(id))
    post.from_json(request.json)
    post.save()
    return make_response(jsonify({'posts':post.to_json()}), 201)


@app.route('/api/posts/delete/<id>', methods=['DELETE'])
def delete_post(id):
    Post.objects(id=ObjectId(id)).delete()
    return make_response("post deleted", 204)


@app.route('/api/posts/create', methods=['POST'])
def new_post():
    post=Post.from_json(request.json)
    post.save()
    return jsonify(post.to_json())


@app.route('/api/users')
def get_users():
    users=User.objects.all()
    return make_response(jsonify({'users':[user.to_json() for user in users]}), 200)


@app.route('/api/users/<id>')
def get_user(id):
    user=User.objects(id=ObjectId(id))
    return jsonify({'user':user.to_json()})


@app.route('/api/users/create', methods=['POST'])
def create_user():
    user=User.from_json(request.json)
    user.save()
    return jsonify(user.to_json())      



#Delete
# Update    