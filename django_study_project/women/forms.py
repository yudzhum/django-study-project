from django import forms
from django_study_project.women import models


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Choose category'

    class Meta:
        model = models.Women
        fields = ['name', 'slug', 'content', 'photo', 'is_published', 'cat']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise forms.ValidationError('Length more than 200 symbols')   
        
        return name
