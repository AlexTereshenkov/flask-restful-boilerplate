"""Application main entrance point."""

import sys
import os
sys.path.append(os.getcwd())

from flask import Flask
from flask_restful import Api
from api.resource import Sum, SumEndpoints
from api.root import Root
from src.config import PORT

if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Root, '/')
    api.add_resource(Sum, f'/{SumEndpoints.GETSUM}')
    app.run(port=PORT)
