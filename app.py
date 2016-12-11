#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from random import randint

import bottle
from bottle import default_app, request, route, response, get, post, template

bottle.debug(True)

def index():
	return template('index.tpl')

bottle.run(host='0.0.0.0', port=argv[1])
