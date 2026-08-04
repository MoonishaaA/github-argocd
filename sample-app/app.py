from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
Sample Application\n

This application has been successfully deployed using Argo CD.\n

Welcome to the GitOps Demo.\n
"""

@app.route("/health")
def health():
    return "Application is Healthy", 200
