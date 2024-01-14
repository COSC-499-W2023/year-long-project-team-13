from django import forms
from . models import VidStream, VidRequest

class VidUploadForm(forms.ModelForm):

    class Meta:
        model = VidStream
        fields = ["title","description", "video"]

class VidRequestForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20, 'style': 'boarder: 2px groove lightgreen;','required': True}))

    class Meta:
        model = VidRequest
        fields = ["reciever","description", "due_date"]
