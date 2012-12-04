#coding=utf-8
from uliweb import expose, function
from cms.models import *
from forms import *
require_login = function('require_login')


@expose('/admin')
def admin():
	if require_login():
		return redirect(url_for(login))	
	if request.method == 'GET':
		site = siteinfo.get(siteinfo.c.id == 1)
		if site is None:
			siteform = siteinfoForm(action='/admin/siteinfo_edit')
		else:	
			siteform = siteinfoForm(action="/admin/siteinfo_edit",data={'name':site.name,\
				'url':site.url,'desc':site.desc,'temp':site.temp,'logo':site.logo})
		category_all = category.all()
		categoryform = categoryForm(action='/admin/category_new')
	return {'siteform':siteform,'category_all':category_all,'categoryform':categoryform}

@expose('/admin/siteinfo_edit')
def siteinfo_edit():
	if require_login():
		return redirect(url_for(login))	
	if request.method == 'POST':
		form = siteinfoForm()
             	flag = form.validate(request.params)
		if flag:
			n = siteinfo(**form.data)
			if siteinfo.get(siteinfo.c.id == 1):
				n.id = 1
			n.save()

	return redirect('/admin')

@expose('/admin/category_new')
def category_new():
	if require_login():
		return redirect(url_for(login))	
	if request.method == 'POST':
		form = categoryForm()
             	flag = form.validate(request.params)
		if flag:
			n = category(**form.data)
			n.save()
	return redirect('/admin')

#########################################################

@expose('/admin/category_list/<id>')
def category_list(id):
	if require_login():
		return redirect(url_for(login))	
	content_form = contentForm(action='/admin/content_new',data={'cateid':id})
	if request.method == 'GET':
		cate_list = content.filter(content.c.cateid == id)
		n = category.get(category.c.id == id)
		name = n.name
	return {'cate_list':cate_list,'content_form':content_form,'name':name}

@expose('/admin/content_new')
def content_new():
	if require_login():
		return redirect(url_for(login))	
	if request.method == 'POST':
		form = contentForm()
             	flag = form.validate(request.params)
		if flag:
			n = content(**form.data)
			id = n.cateid
			n.save()	
	return redirect('/admin/category_list/'+str(id))
