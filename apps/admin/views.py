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
			siteform = siteinfoForm()
		else:	
			siteform = siteinfoForm(data={'name':site.name,\
				'url':site.url,'desc':site.desc,'temp':site.temp,'logo':site.logo})
		category_all = category.all()
		categoryform = categoryForm()
	return {'siteform':siteform,'category_all':category_all,'categoryform':categoryform}
