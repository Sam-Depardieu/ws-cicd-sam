import os
import socket

from flask import Flask, jsonify

app = Flask(__name__)

# Message affiché sur la page d'accueil : à modifier pendant le workshop (Sam)
MESSAGE = "Bonjour depuis mon pipeline CI/CD ! (Sam)"
# Version injectée au build (SHA du commit en CI, "dev" par défaut)
VERSION = os.getenv("APP_VERSION", "dev")


@app.route("/")
def index():
    return (
        f"<h1>{MESSAGE}</h1>\n"
        f"<p>Version : <code>{VERSION[:7]}</code></p>\n"
        f"<p>Conteneur : <code>{socket.gethostname()}</code></p>\n"
    )


@app.route("/health")
def health():
    return jsonify(status="ok", version=VERSION)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
