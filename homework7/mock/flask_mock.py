import os
import threading

from flask import Flask, jsonify, request

from homework7 import settings

app = Flask(__name__)
SURNAME_DATA = {}

app.route("/get_surname/<name>", methods=["GET"])
def get_user_surname(name):
    if surname := SURNAME_DATA.get(name):
        return jsonify(surname), 200
    else:
        return jsonify(f"Surname for user {name} not found"), 404


def shutdown_stub():
    # Этот код будет работать на старой версии сервера werkzeug
    terminate_func = request.environ.get("werkzeug.server.shutdown")
    if terminate_func:
        terminate_func()


@app.route("/shutdown")
def shutdown():
    shutdown_stub()
    return jsonify("Ok, exiting"), 200


def run_mock():
    # для завершения процесса Thread нужно использовать werkzeug
    # Запуск тестов изнутри, доступны глобальные переменные
    server = threading.Thread(
        target=app.run, kwargs={"host": settings.MOCK_HOST, "port": settings.MOCK_PORT}
    )
    server.start()
    return server

# if __name__ == "__main__":
#     host = os.environ.get("MOCK_HOST", "127.0.0.1")
#     port = os.environ.get("MOCK_PORT", "8082")
#     app.run(host, port)