#coding=utf-8
from uliweb import expose, functions
from models import *


@expose('/')
def index():
	site        = siteinfo.get(siteinfo.c.id == 1)
	cate        = category.all()
	return {'site':site,'cate':cate}

def category_content(id,limit=10):
	cate_cont = content.filter(content.c.cateid == id).limit(limit)
	return cate_cont 

def category_get(limit=10):
	cate_name = category.all().limit(limit)
	return cate_name 
