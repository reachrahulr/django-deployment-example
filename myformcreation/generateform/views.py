from django.shortcuts import render
from . import forms
from . import newform


def index(request):
    return render(request, 'index.html')

def form_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Validation success')
            print('Name: ' +form.cleaned_data['name'])

    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def signup(request):

    form = newform.NewUserForm()

    if request.method == "POST":
        form = newform.NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'signuppage.html',{'form':form})
