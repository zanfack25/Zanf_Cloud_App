from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # enable CORS if needed


@app.route('/')
def hello_cloud():
    return 'Hello from David Roland ECS Container !'

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
