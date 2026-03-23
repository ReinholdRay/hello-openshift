from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello OpenShift</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: #f0f4f8; }
        .card { background: white; border-radius: 12px; padding: 48px 64px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); text-align: center; }
        h1 { color: #cc0000; margin-bottom: 8px; }
        p { color: #555; font-size: 1.1em; }
        .badge { margin-top: 24px; display: inline-block; background: #cc0000; color: white; padding: 6px 16px; border-radius: 20px; font-size: 0.9em; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Hello from OpenShift!</h1>
        <p>Your application is running successfully.</p>
        <div class="badge">Deployed by ReinholdRay</div>
    </div>
</body>
</html>"""

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
