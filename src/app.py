from flask import Flask, jsonify, request, abort

from src.errors.errors import handle_400, InvalidCall
from src.services.hatchway_client.hatchway_client_strategy import HatchwayClientStrategy

app = Flask(__name__)

app.register_error_handler(InvalidCall, handle_400)
hc = HatchwayClientStrategy.getClient("real")

@app.route("/api/ping")
def ping():
    data = {"success": "true"}
    return jsonify(data), 200

@app.route("/api/posts")
def posts():
    tags = request.args.getlist('tags')
    if not tags:
        raise InvalidCall("Tags parameter is required")

    sort_by_query = request.args.get('sortBy')
    direction_query = request.args.get('direction')

    if sort_by_query and sort_by_query not in ['id', 'reads', 'likes', 'popularity']:
        raise InvalidCall("sortBy parameter is required")
    if direction_query and direction_query not in ['asc', 'desc']:
        raise InvalidCall("direction parameter is required")
    
    sort_by = sort_by_query if sort_by_query else 'id'
    direction = True if direction_query=='asc' else False
    res = hc.get_posts(tags, sort_by, direction)
    data = {"posts": res}
    return jsonify(data), 200
