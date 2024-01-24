from flask import Flask, request, jsonify
from functions_api import  edge_followed_by_count , post_likes_count,post_comments_count

app = Flask(__name__)

# this is allowed ips
allowed_ips = ["162.159.140.98", "172.66.0.96", "2606:4700:7::60", "2a06:98c1:58::60"]

@app.before_request
def check_security():
    client_ip = request.remote_addr
    print(f"client_ip : {client_ip}")
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