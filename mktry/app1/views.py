# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext,loader
from .models import try_carousel
from .forms import test_form

def add(request):
    if request.method == "POST": #执行添加
        tf = test_form(request.POST,request.FILES)
        if tf.is_valid():
            # 获取表单数据
            title = tf.cleaned_data['title']
            type = tf.cleaned_data['type']
            sort = tf.cleaned_data['sort']
            link_url = tf.cleaned_data['link_url']
            img_url = tf.cleaned_data['img_url']
            # 保存到数据库
            tc = try_carousel()
            tc.title = title
            tc.type = type
            tc.sort = sort
            tc.link_url = link_url
            tc.img_url = img_url
            tc.save()
            return HttpResponse('添加成功!')
    else: #展示空表单
        return render(request,'app1/add.html',{'form':test_form()})

def delete(request):
    '把state字段置为1'
    id = request.GET['id']
    res = try_carousel.objects.get(id=id)
    res.state = 1
    res.save()
    return HttpResponse(r'删除成功！<a href="/app1/">返回首页</a>')

def update(request):
    if request.POST:
        res = try_carousel.objects.get(id=request.GET['id'])
        res.title = request.POST['title']
        res.type = request.POST['type']
        res.sort = request.POST['sort']
        res.img_url = request.POST['img_url']
        res.link_url = request.POST['link_url']
        res.save()
        return HttpResponse(r'更新成功！')
    else:
        tc = try_carousel.objects.get(id=request.GET['id'])
        return render(request,'app1/update.html',{'tc':tc,'id':request.GET['id']})

def list(request):
    content_list = try_carousel.objects.filter(state=0)
    return render(request,'app1/list.html',{'content_list':content_list})