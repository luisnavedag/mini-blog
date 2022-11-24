from .models import EditorForm
from django import forms


class EditorFM(forms.ModelForm):
    
    class Meta:
        model = EditorForm
        fields = ['subject','message','portfolio_url','resume']
        enctype= "multipart/form-data"
       
        
    def __init__(self, *args, **kwargs):
        super(EditorFM, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})