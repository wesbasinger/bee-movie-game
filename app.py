#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from game import Game

import bottle
from bottle import default_app, request, route, response, get, post, template

bottle.debug(True)

@get('/')
def index():
    g = Game()
    l = g.scramble(0)
    return template('index.tpl', scramble_dict=l)

@get('/play/<line_num>/<streak>')
def play(line_num, streak):
    return(line_num)

@post("/check/missing/<word>")
def check(word):
    answer = request.forms["answer"]
    if answer == word:
        print("right")
    
    
     

bottle.run(host='0.0.0.0', port=argv[1])
