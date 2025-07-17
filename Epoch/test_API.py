from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data
items = [
    {"id": 1, "name": "Widget", "price": 10.99},
    {"id": 2, "name": "Gadget", "price": 12.49}
]

# GET /items - list all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET /items/<id> - get one item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    return jsonify(item) if item else ("Not found", 404)

# POST /items - create a new item
@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": data["name"],
        "price": data["price"]
    }
    items.append(new_item)
    return jsonify(new_item), 201

# PUT /items/<id> - update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    item = next((item for item in items if item["id"] == item_id), None)
    if not item:
        return "Not found", 404
    item.update(data)
    return jsonify(item)

# DELETE /items/<id> - delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return '', 204

# Start the server
if __name__ == '__main__':
    app.run(debug=True)