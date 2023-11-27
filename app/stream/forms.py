from django import forms
from . models import VidStream

class VidUploadForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))

    class Meta:
        model = VidStream
        fields = ["title","description", "video"]
