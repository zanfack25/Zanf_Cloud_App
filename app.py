from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
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
    # Return a simple 200 OK response
    return 'OK', 200
app = Flask(__name__)

if __name__ == '__main__':
    # Keep port consistent with ECS/ALB config
    app.run(host='0.0.0.0', port=80)
