from django import forms
from .models import try_carousel
class test_form(forms.Form):
    type = forms.CharField(label='type',max_length=100)
    title = forms.CharField(label='title',max_length=100)
    link_url = forms.CharField(label='link_url',max_length=100)
    img_url = forms.CharField(label='img_url',max_length=100)
    sort = forms.CharField(label='sort',max_length=100)
    # upload_img = forms.CharField(label='upload_img',max_length=100)
    class Meta:
        model = try_carousel