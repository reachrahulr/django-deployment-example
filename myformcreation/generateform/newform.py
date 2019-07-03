from django import forms
from .models import User

class NewUserForm(forms.ModelForm):
    verifyemail = forms.EmailField(label='Enter your mail again')

    def clean(self):
        allclean =  super().clean()
        originalemail = allclean['email']
        vamil = allclean['verifyemail']

        if originalemail != vamil:
            raise forms.ValidationError('mails are not equal')

    class Meta():
        model = User
        fields = '__all__'
