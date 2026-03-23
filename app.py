from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello from OpenShift!</h1><p>Deployed by ReinholdRay</p>"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/api/info")
def info():
    return jsonify({
        "app": "hello-openshift",
        "status": "running",
        "deployed_by": "ReinholdRay"
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
