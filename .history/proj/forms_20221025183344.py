from django import  forms
from django.forms import ModelForm, widgets
from .models import Project,Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title","featured_image","description","demo_link",
                  "source_link","tags"]
        widgets = {
            "tags":forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["value","vote"]
        
        