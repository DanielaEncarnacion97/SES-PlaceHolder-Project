#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging as logger
from flask import Blueprint, jsonify, request
from scraper import get_walmart, get_target
import json

main = Blueprint('main', __name__)
print('App is startign!!')


@main.route('/api/<data>', methods=['POST', 'GET'])
def api(data):
    print('Startign service')
    #  data = request.get_json()
    
    try:
        print('-'*80)
        print(data)
        print('-'*80)

        data = data.split(',')

        # Body
        print('Running')

        output = []
        for datum in data:
            output.append((datum, 10))

        return jsonify(output)

    except Exception as e:
        print('Found exception', e)
        return "Error" , 400
