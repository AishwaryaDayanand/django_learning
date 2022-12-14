from dataclasses import field
from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = "__all__"  # can put particular fields needed in list
        fields = ["title", "featured_imgs", "description", "demo_link", "source_link" , "tags"  ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),  # make tags field as checkbox 
            # 'title': forms.Textarea()             # make title field as textarea 
        }

    def __init__(self,*args , **kwargs ):
        super(ProjectForm , self).__init__(*args , **kwargs )


        for name , field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        # self.fields['title'].widget.attrs.update({'class':'input111'})  -- update only needed elememt
