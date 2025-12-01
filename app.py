from flask import Flask
from flask_cors import CORS

app = Flask(__name__)


@app.route('/')
def hello_cloud():
    return 'Hello from David Roland ECS Container !'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
