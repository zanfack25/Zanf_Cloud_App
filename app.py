from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_cloud():
    return 'Hello from David Roland ECS Container !'

@app.route('/health')
def health():
    # Return a simple 200 OK response
    return 'OK', 200

if __name__ == '__main__':
    # Keep port consistent with ECS/ALB config
    app.run(host='0.0.0.0', port=5000)
