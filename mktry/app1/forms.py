# coding=utf-8
from django import forms
from .models import try_carousel
class test_form(forms.Form):
    YEAR_IN_SCHOOL_CHOICES = (
        ('1', '首页'),
        ('2', '试用报告首页'),
    )
    type = forms.ChoiceField(widget=forms.Select,choices=YEAR_IN_SCHOOL_CHOICES)
    title = forms.CharField(label='title',max_length=100)
    link_url = forms.CharField(label='link_url',max_length=100)
    sort = forms.IntegerField()
    img_url = forms.FileField()
    class Meta:
        model = try_carousel