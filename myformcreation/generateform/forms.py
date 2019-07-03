from django import forms
from django.core import validators

#your own validation creator

def check_for_z(value):
    if value[0].lower() == 'z':
        raise forms.ValidationError('name should not start with z')

def maximum(value):
    if len(value) < 3:
        raise forms.ValidationError('summary should need more than 3 characters length')

class FormName(forms.Form):
    name = forms.CharField(validators= [check_for_z])
    email = forms.EmailField()
    verifyemail = forms.EmailField(label='Enter your mail again')
    summary = forms.CharField(widget= forms.Textarea, validators= [maximum])
    botcatcher = forms.CharField(required=False, widget= forms.HiddenInput, validators= [validators.MaxLengthValidator(0)])


    def clean(self):
        allclean =  super().clean()
        originalemail = allclean['email']
        vamil = allclean['verifyemail']

        if originalemail != vamil:
            raise forms.ValidationError('mails are not equal')
