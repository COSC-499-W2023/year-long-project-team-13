from django import forms
from . models import VidStream
from . models import VidRequest

class VidUploadForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))

    class Meta:
        model = VidStream
        fields = ["title","description", "video"]

class VidRequestForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))

    class Meta:
        model = VidRequest
        fields = ["reciever","description", "due_date"]
