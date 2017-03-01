#!/usr/bin/python

import httplib

from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def query():
    return Response("Hello World\n", httplib.OK)


if __name__ == '__main__':
    app.run(port=8888, debug=True)
