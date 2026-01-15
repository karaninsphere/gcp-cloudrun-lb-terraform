from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Cloud Run behind Load Balancer 🚀\n"

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/info")
def info():
    return jsonify(
        service="cloudrun-sample-app",
        project=os.environ.get("GOOGLE_CLOUD_PROJECT"),
        revision=os.environ.get("K_REVISION")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
