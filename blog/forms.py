from django import forms
from django.forms import ModelForm
from base.models import *


class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['created_on', 'is_visible','creator_rating']  # not attachments!
        widgets = {
            'description': forms.Textarea(attrs={'class': 'input-field'}),

        }

    def __init__(self, *args, **kwargs):
        super(AddBlogForm, self).__init__(*args, **kwargs)
        self.fields['description'].required=True
        self.fields['title'].required=True

    def save(self, commit=True):
        instance = super(AddBlogForm, self).save(commit=False)
        instance.save(commit)

        return instance
