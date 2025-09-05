from django import forms
from .models import Focus
from django.contrib.auth.models import User

class Focusform (forms.ModelForm):
    class Meta:
        model = Focus
        fields = ['title','srno']
    # title = forms.CharField(max_length= 200)
    # srno=forms.AutoField(Primary_key = True , auto_created=True,editable=False)
    # date= forms.DateField(auto_now_add= True)
    # user= forms.ForeignKey(User , on_delete = models.CASCADE)
        