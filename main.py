import os
from flask import Flask, request, jsonify, make_response
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GKE_API_URL = os.getenv("GKE_API_URL", "http://localhost:8080")

@app.route('/<path:path>', methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])
def proxy(path):
    url = f"{GKE_API_URL}/{path}"
    
    headers = {key: value for key, value in request.headers if key != 'Host'}
    data = request.get_data() if request.method in ['POST', 'PUT', 'PATCH'] else None
    
    try:
        if request.method == "GET":
            response = requests.get(url, headers=headers, params=request.args)
        elif request.method == "POST":
            response = requests.post(url, headers=headers, data=data)
        elif request.method == "PUT":
            response = requests.put(url, headers=headers, data=data)
        elif request.method == "DELETE":
            response = requests.delete(url, headers=headers)
        elif request.method == "PATCH":
            response = requests.patch(url, headers=headers, data=data)
        elif request.method == "OPTIONS":
            response = requests.options(url, headers=headers)
        elif request.method == "HEAD":
            response = requests.head(url, headers=headers)
        else:
            return jsonify({"error": "Método HTTP no soportado"}), 405
        
        response_content = response.content
        response_headers = dict(response.headers)
        
        flask_response = make_response(response_content, response.status_code)
        flask_response.headers = response_headers
        
        return flask_response

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)