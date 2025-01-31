from django import forms

class BlogForm(forms.Form):
    topic = forms.CharField(max_length=255, label="Enter Blog Topic")
