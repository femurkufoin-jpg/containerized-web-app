from flask import jsonify


def register_routes(app):
    visits = {"count": 0}

    @app.get("/health")
    def health():
        return jsonify({"status": "healthy"})

    @app.get("/visits")
    def get_visits():
        visits["count"] += 1
        return jsonify({"visits": visits["count"]})