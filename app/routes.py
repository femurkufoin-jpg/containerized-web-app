import os

import redis
from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    redis_host = os.getenv("REDIS_HOST", "localhost")
    redis_port = int(os.getenv("REDIS_PORT", "6379"))

    redis_client = redis.Redis(
        host=redis_host,
        port=redis_port,
        decode_responses=True,
    )

    @app.get("/health")
    def health():
        return jsonify({"status": "healthy"})

    @app.get("/visits")
    def get_visits():
        count = redis_client.incr("visits")
        return jsonify({"visits": count})

    return app