#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from game import Game

import bottle
from bottle import default_app, request, route, response, get, post, template,redirect, static_file

bottle.debug(True)

@get('/')
def index():
    g = Game()
    l = g.scramble(0)
    return template('index.tpl', scramble_dict=l, streak=0)

@get('/play/<line_num>/<streak>')
def play(line_num, streak):
    g = Game()
    l = g.scramble(int(line_num))
    return template('index.tpl', scramble_dict=l, streak=streak)

@post("/check/missing/<word>/line/<line_num>/streak/<streak>")
def check(word, line_num, streak):
    next_line = int(line_num) + 1
    answer = request.forms["answer"]
    if answer == word:
        new_streak = int(streak) + 1
        redirect("/play/"+str(next_line)+"/"+str(new_streak))
    else:
        redirect("/play/"+str(next_line)+"/0")
    
@route('/images/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root='/User/teacher/Google\ Drive/code/bee-movie-game', mimetype='image/jpg')    
     

bottle.run(host='0.0.0.0', port=argv[1])
