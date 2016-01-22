from django.shortcuts import render
from django.http import HttpResponse
from .models import try_carousel
from django.template import RequestContext,loader
from .forms import test_form

def add(request):
    'display a empty form'
    return render(request,'app1/add.html',{'form':test_form()})

def add1(request):
    'do add action'
    # Todo:change to variable
    # csl = try_carousel(title='aaa',type=1,sort=1,img_url='a.jpg',link_url='http://try.makepolo.com')
    title = request.POST['title']
    type = request.POST['type']
    sort = request.POST['sort']
    img_url = request.POST['img_url']
    link_url = request.POST['link_url']

    csl = try_carousel(title=title,type=type,sort=sort,img_url=img_url,link_url=link_url)
    # form = test_form({'title':title,'type':type,'sort':sort,'img_url':img_url,'link_url':link_url})
    csl.save()
    return HttpResponse(r'add ok')

def delete(request):
    'update state field to 1.'
    id = request.GET['id']
    res = try_carousel.objects.get(id=id)
    res.state = 1
    res.save()
    return HttpResponse(r'delete ok')

def update(request):
    'display a form with data from mysql'
    # res = try_carousel.objects.filter(id=1)
    res = {'title':'aaa','type':1,'sort':1,'img_url':'a.jpg','link_url':'http://try.makepolo.com'}
    form = test_form(res)
    return render(request,'app1/update.html',{'form':form,'id':request.GET['id']})

def update1(request):
    'do update action'
    res = try_carousel.objects.get(id=request.GET['id'])
    res.title = request.POST['title']
    res.type = request.POST['type']
    res.sort = request.POST['sort']
    res.img_url = request.POST['img_url']
    res.link_url = request.POST['link_url']
    res.save()
    return HttpResponse(r'update ok')

def list(request):
    'list all data from mysql'
    content_list = try_carousel.objects.all()
    return render(request,'app1/list.html',{'content_list':content_list})