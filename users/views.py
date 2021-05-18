from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from .decorators import unathenticated_user
# Create your views here.


@unathenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username ,password = password )
        if user != '' and user is not None:
            login(request,user)
            return redirect('books:index')
        else:
            pass
    else:
        form = AuthenticationForm()
    return render(request , 'users/login.html', {'form':form})

def logout_page(request):
    logout(request)
    return redirect('users:login')

def signup_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()
        print(form)
    return render(request ,'users/signup.html',{'form':form})

