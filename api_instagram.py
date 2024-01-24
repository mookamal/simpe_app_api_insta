from flask import Flask, request, jsonify
from functions_api import  edge_followed_by_count , post_likes_count,post_comments_count

app = Flask(__name__)

allowed_ips = ["127.1.1.1"]

@app.before_request
def check_security():
    client_ip = request.remote_addr

    if not client_ip in allowed_ips:
        return jsonify({"error": "Unauthorized access"}), 401 

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