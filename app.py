from flask import Flask
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app)  # enable CORS if needed

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

@app.route('/host')
def host_name():
    return hostname

@app.route('/ip')
def host_ip():
    return ip_address

@app.route('/')
def hello_cloud():
    return 'Hello from David Roland ECS Container !'

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
