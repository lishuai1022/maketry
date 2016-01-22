#__author__ = 'min'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/',views.add,name='add'),
    url(r'^add1/',views.add1,name='add1'),
    url(r'^delete/',views.delete,name='delete'),
    url(r'^update/',views.update,name='update'),
    url(r'^update1/',views.update1,name='update1'),
    url(r'^$',views.list,name='list'),
]
