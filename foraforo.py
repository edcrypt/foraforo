#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bottle import route, run, template
import random

sandices = open('sandices.txt', 'r').readlines()


def foraforoforofora():
    b = ['FORO', 'FORA'] * 2
    random.shuffle(b)
    return '! '.join(b)


def sandice_aleatoria():
    return random.choice(sandices)


@route('/')
def index():
    sandice = sandice_aleatoria()
    fora = foraforoforofora()
    return template('foraforo', **locals())

run(host='0.0.0.0', port=8081)
