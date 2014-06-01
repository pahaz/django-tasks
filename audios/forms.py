from django import forms
from audios.models import Audio

# ModelForms, step12

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ('author', 'name', 'file')