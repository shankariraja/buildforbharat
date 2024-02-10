# webapp/forms.py
from django import forms

class PhotoUploadForm(forms.Form):
    photo1 = forms.ImageField(label='Upload Photo 1')
    photo2 = forms.ImageField(label='Upload Photo 2')
