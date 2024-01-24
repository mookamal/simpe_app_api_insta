from flask import Flask, request, jsonify
from functions_api import  edge_followed_by_count , post_likes_count,post_comments_count

app = Flask(__name__)

@app.route('/followed_count', methods=["GET"])
def get_followed_count():
    username = request.args.get("username")
    count = edge_followed_by_count(username)
    return jsonify({"count":count})


@app.route('/post_likes_count', methods=["GET"])
def get_post_likes_count():
    post_id = request.args.get("post_id")
    count = post_likes_count(post_id)
    return jsonify({"count":count})

@app.route('/post_comments_count', methods=["GET"])
def get_post_comments_count():
    post_id = request.args.get("post_id")
    count = post_comments_count(post_id)
    return jsonify({"count":count})


if __name__ == '__main__':
    app.run(debug=True, port=5000)