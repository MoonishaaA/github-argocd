from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
Sample Application

This application has been successfully deployed using Argo CD.

Welcome to the GitOps Demo.
"""

@app.route("/health")
def health():
    return "Application is Healthy", 200
