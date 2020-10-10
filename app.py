# -*- coding: utf-8 -*-

from flask import Flask
from util import *


app = Flask(__name__)
logger = Logger.debug_logger()


@app.route("/")
def home():
    logger.debug("GET / (home)")
    return "Home"


if __name__ == '__main__':
    logger.debug("Run Application")
    app.run(host='0.0.0.0', port=8080, debug=True)
