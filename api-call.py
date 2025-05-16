from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import json
import platform
import socket

app = Flask(__name__)
CORS(app)  # Allows requests from any origin

@app.route('/status', methods=['GET'])
def api_connect():
    return jsonify({"status": "ok"}), 200

@app.route('/', methods=['POST'])
def execue_model():
    try:
        # Receives data from any source
        received_data = request.get_json()

        # Print the received data (Debug Only)
        print('Dados Recebidos:', received_data)
        
        if not received_data:
            return jsonify({"error": "No JSON found."}), 400

        # Converts the JSON into string and passes as a argument
        args_json = json.dumps(received_data)

        # Run the navis.py with the data
        result = subprocess.run(
            ["python", "navis.py", args_json],
            capture_output=True,
            text=True,
            check=True
        )

        # Returns the output and standart error 
        return jsonify({
            'return_code': result.returncode,
            'output': result.stdout.strip(),
            'error': result.stderr.strip(),
        }), 200 if result.returncode == 0 else 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
