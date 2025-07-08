from flask import Flask, request, jsonify

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"}
]

@app.route('/')
def home():
    return "Server is running!"

@app.route('/items', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_items():
    if request.method == 'GET':
        print("GET request received")
        # return jsonify({"message": "List of items", "items": items})
        return jsonify({"items": items, "message": "List of items"})

    elif request.method == 'POST':
        new_item = request.get_json()
        print("POST request received:", new_item)
        items.append(new_item)
        return jsonify({"message": "Item added", "item": new_item, "items": items}), 201

    elif request.method == 'PUT':
        updated_item = request.get_json()
        print("PUT request received:", updated_item)
        for item in items:
            if item['id'] == updated_item['id']:
                item['name'] = updated_item['name']
                return jsonify({"message": "Item updated", "item": item, "items": items})
            elif request.method == 'PUT':
                 updated_item = request.get_json()
                 print("PUT data received:", updated_item)

        return jsonify({"message": "Item not found"}), 404

    elif request.method == 'DELETE':
        data = request.get_json()
        item_id = data.get('id')
        print("DELETE request received for id:", item_id)
        for i, item in enumerate(items):
            if item['id'] == item_id:
                deleted = items.pop(i)
                return jsonify({"message": "Item deleted", "item": deleted, "items": items})
        return jsonify({"message": "Item not found"}), 404

'''if __name__ == '__main__':
    app.run(debug=True, port=6000)'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)