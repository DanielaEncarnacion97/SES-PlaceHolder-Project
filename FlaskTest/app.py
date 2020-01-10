#!/usr/bin/env python
# -- coding: utf-8 --
from flask import Blueprint, jsonify, request
from scraper import get_walmart, get_target
import json
import sys
main = Blueprint('main', _name_)
print('App is startign!!')
@main.route('/api/<data>', methods=['POST', 'GET'])
def items_processor(data):
    try:
        class Item:
            def _init_(self, name, cost, supplier):
                self.name = name
                self.cost = cost
                self.supplier = supplier
                self.isCheaper = None
            def setIsCheaper(self, isCheaper):
                self.isCheaper = isCheaper
            def getCost(self):
                return self.cost
            def _dict_(self):
                return {"name": self.name, "cost": self.cost, "supplier": self.supplier, "isCheaper": self.isCheaper}
        def find_min_relevant(options, item, supplier):
            for (name,cost) in options:
                if item in name.lower() or item[:-1] in name.lower():
                    return Item(name, cost, supplier)
            return Item("Error: no relevant items", sys.float_info.max, supplier)
        def is_target_cheaper(result, target_item, walmart_item):
            target_item.setIsCheaper(result)
            walmart_item.setIsCheaper(not(result))
        item_list = []
        data = data.split(',')
        data = filter(None, data)
        for item in data:
            item = item.strip().lower()
            walmart_options = get_walmart(item)
            target_options = get_target(item)
            walmart_item = find_min_relevant(walmart_options, item, 'walmart')
            target_item = find_min_relevant(target_options, item, 'target')
            if walmart_item.getCost() > target_item.getCost():
                is_target_cheaper(True, target_item, walmart_item)
            else:
                is_target_cheaper(False, target_item, walmart_item)
            item_list.append(target_item._dict_())
            item_list.append(walmart_item._dict_())
        return jsonify(item_list)
    except Exception as e:
        print('Found exception', e)
        return "Error" , 400
import pprint
data = 'bread,eggs'
pprint.pprint(items_processor(data))
