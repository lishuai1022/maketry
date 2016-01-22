# coding=utf-8
from django import forms
from .models import try_carousel
class test_form(forms.Form):
    YEAR_IN_SCHOOL_CHOICES = (
        ('1', '首页'),
        ('2', '试用报告首页'),
    )
    type = forms.ChoiceField(widget=forms.Select,choices=YEAR_IN_SCHOOL_CHOICES,label='类型')
    title = forms.CharField(label='标题',max_length=100)
    link_url = forms.CharField(label='链接地址',max_length=100)
    sort = forms.IntegerField(label='排序')
    img_url = forms.FileField(label='图片地址')
    class Meta:
        model = try_carousel