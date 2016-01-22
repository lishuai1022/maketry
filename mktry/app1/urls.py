#__author__ = 'min'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/',views.add,name='add'),
    url(r'^delete/',views.delete,name='delete'),
    url(r'^update/',views.update,name='update'),
    url(r'^$',views.list,name='list'),
]
