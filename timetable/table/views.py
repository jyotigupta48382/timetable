from .form import CreateUserForm
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.decorators import login_required
from  django.contrib.auth import authenticate, login, logout



''' 
"superuser":"timetable",
"password":"timetable"
"user_name:user_password@123"
'''


'''Register page '''
def registerPage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+user)
            return redirect('login')
    context={'form':form}
    return render(request,'accounts/register.html',context)


'''Login page'''
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'UserName or Password is incorrect')

    context={}
    return render(request,'accounts/login.html',context)



'''Logout Page '''
def logoutPage(request):
    logout(request)
    return redirect('login')





'''home Page '''
@login_required(login_url='login')
def homePage(request):
    context={}
    return render(request,'accounts/home.html',context)