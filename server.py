from crypt import methods
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

@app.route("/", methods=["POST"])
def main():
    try:
        length = int(request.form.get('length'))
    except Exception as e:
        return jsonify({'message': 'Invalid request'}), 500

    result = jsonify({'Server': "Operational", 'Received Data': length})

    return result



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")