#coding=utf-8

from uliweb.form import *

class siteinfoForm(Form):
        name   = StringField(label="站点名称",required=True)
        url    = StringField(label="域名")
        desc   = TextField(label="简短描述",required=True,rows=5,cols=30)
        #title  = StringField(label="站点名称")
        temp   = StringField(label="模板名称")
        logo   = StringField(label="logo图片")

class categoryForm(Form):
        id_order = StringField(label="排序",default=0)
        name     = StringField(label="模块")
        temp     = StringField(label="模板名称",required=True)
        image    = StringField(label="图片")

class contentForm(Form):
        id_order = StringField(label="排序",default=0)
        title    = StringField(label="标题",required=True)
        content  = StringField(label="内容",required=True)
        image    = StringField(label="图片")

