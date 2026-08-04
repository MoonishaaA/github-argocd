from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>GitOps Demo</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: #f4f4f4;
                font-family: Arial, sans-serif;
            }

            .container {
                text-align: center;
            }

            h1 {
                color: #2c3e50;
                margin-bottom: 20px;
            }

            p {
                font-size: 20px;
                margin: 10px 0;
                color: #34495e;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Sample Application</h1>
            <p>This application has been successfully deployed using Argo CD.</p>
            <p>Welcome to the GitOps Demo.</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return "Application is Healthy", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
