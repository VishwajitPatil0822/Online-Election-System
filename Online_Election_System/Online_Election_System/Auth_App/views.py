from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def signup_view(request):
    template_name = 'Auth_App/signup.html'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_registration_view_url')
    context = {'form':form}
    return render(request, template_name, context)

def login_view(request):
    template_name = 'Auth_App/login.html'
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = authenticate(username=un,password=pw)
        print('username -->',un,'password -->',pw)
        if user is not None:
            login(request,user)
            return redirect('show_registration_view_url')
    context = {}
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('login_view_url')