from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

tasks = []


if __name__ == '__main__':
    app.run(degug=True)