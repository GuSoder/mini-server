from flask import Flask, request, jsonify

app = Flask(__name__)

# Array of networked objects
networked_objects = [
    {"pos_x": 0.0, "pos_y": 0.0, "pos_z": 0.0, "rot_y": 0.0},
    {"pos_x": 0.0, "pos_y": 0.0, "pos_z": 0.0, "rot_y": 0.0},
    {"pos_x": 0.0, "pos_y": 0.0, "pos_z": 0.0, "rot_y": 0.0},
    {"pos_x": 0.0, "pos_y": 0.0, "pos_z": 0.0, "rot_y": 0.0},
    {"pos_x": 0.0, "pos_y": 0.0, "pos_z": 0.0, "rot_y": 0.0},
    {"pos_x": 0.0, "pos_y": 0.0, "pos_z": 0.0, "rot_y": 0.0}
]

@app.route('/object/<int:index>', methods=['GET'])
def get_object(index):
    if 0 <= index < len(networked_objects):
        return jsonify(networked_objects[index])
    return jsonify({"error": "Invalid index"}), 404

@app.route('/object/<int:index>', methods=['POST'])
def post_object(index):
    if 0 <= index < len(networked_objects):
        data = request.get_json()
        if data and all(key in data for key in ['pos_x', 'pos_y', 'pos_z', 'rot_y']):
            networked_objects[index] = {
                "pos_x": float(data['pos_x']),
                "pos_y": float(data['pos_y']),
                "pos_z": float(data['pos_z']),
                "rot_y": float(data['rot_y'])
            }
            return jsonify({"success": True})
        return jsonify({"error": "Invalid data"}), 400
    return jsonify({"error": "Invalid index"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)