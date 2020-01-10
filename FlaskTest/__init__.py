#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
# CORS is needed to avoid security errors in local host
from flask_cors import CORS 

def create_app():
    app = Flask(__name__)
    app.config['CORS_HEADERS'] = 'Content-Type'
    # cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:8080"}})
    # @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
    cors = CORS(app)
    from app import main
    app.register_blueprint(main)
    print('App registered!!')
    return app
create_app().run()
