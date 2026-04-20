from flask import Flask, request, jsonify
import time

app = Flask(__name__)

latest_data = {
    "value": "0,NONE",
    "time": time.time()
}

@app.route('/update', methods=['POST'])
def update():
    global latest_data
    data = request.json
    latest_data["value"] = data["value"]
    latest_data["time"] = time.time()
    return jsonify({"status": "ok"})

@app.route('/data')
def get_data():
    return jsonify(latest_data)

app.run(host="0.0.0.0", port=8000)