#coding=utf-8
from uliweb import expose, functions
from models import *


@expose('/')
def index():
    return '<h1>Hello, Uliweb</h1>'
