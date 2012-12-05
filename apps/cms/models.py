#coding=utf-8

from uliweb.orm import *

class siteinfo(Model):
	name   = Field(CHAR)
	url    = Field(CHAR)
	desc   = Field(CHAR)
#	title  = Field(CHAR)
	temp   = Field(CHAR)
	logo   = Field(CHAR)

class category(Model):
	id_order = Field(int)
	name     = Field(CHAR)
	num      = Field(int)
	temp     = Field(CHAR)
	image    = Field(CHAR)

class content(Model):
	id_order = Field(int)
	cateid   = Field(int)
	title    = Field(CHAR)
	content  = Field(CHAR)
	image    = Field(CHAR)




