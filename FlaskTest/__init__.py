#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging as logger
from flask import Flask

def create_app():
    app = Flask(__name__)
    from app import main
    app.register_blueprint(main)

    print('App registered!!')
    return app

create_app().run()
