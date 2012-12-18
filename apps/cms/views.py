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

@expose('/category_show/<id>')
def category_show(id):
	site        = siteinfo.get(siteinfo.c.id == 1)
	cate        = category.all()
	cate_info = category.get(category.c.id==id)
	cate_list = content.filter(content.c.cateid == id)
	return {'site':site,'cate':cate,'cate_list':cate_list,'cate_info':cate_info}


def subString(string,length):  
    if length >= len(string):  
        return string  
    result = ''  
    i = 0  
    p = 0  
    while True:  
        ch = ord(string[i])  
        #1111110x  
        if ch >= 252:  
            p = p + 6  
        #111110xx  
        elif ch >= 248:  
            p = p + 5  
        #11110xxx  
        elif ch >= 240:  
            p = p + 4  
        #1110xxxx  
        elif ch >= 224:  
            p = p + 3  
        #110xxxxx  
        elif ch >= 192:  
            p = p + 2  
        else:  
            p = p + 1     
              
        if p >= length:  
            break;  
        else:  
            i = p  
        return string[0:i]  	
