from flask import Flask
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>Cloud DevOps Automation System</h1>

    <p>Status: Running Successfully</p>

    <p>Current Time: {datetime.now()}</p>

    <p>Host: {socket.gethostname()}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)