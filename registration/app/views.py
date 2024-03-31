from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib import messages



def FirstPage(request):
    return render(request, 'firstPage.html')

# def SignupPage(request):
#     if request.method=='POST':
#         uname=request.POST.get('username')
#         email=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')

#         if not (uname and email and pass1 and pass2):
#             return redirect('signup')

#         if pass1!=pass2:
#             # return HttpResponse("Your password and confirm password are different")
#             return redirect('signup')
#         else:
#             my_user=User.objects.create_user(uname,email,pass1)
#             my_user.save()
#             return redirect('login')

#     return render (request, 'signup.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if not (uname and email and pass1 and pass2):
            return redirect('signup')

        if pass1 != pass2:
            return redirect('signup')

        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return redirect('signup')

        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    
    return render(request, 'signup.html')  



def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('registration')
        else:
            message = "Username or Password is incorrect!!!"
            return render(request, 'login.html', {'message': message})

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')

def registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.filled_by = request.user
            registration.save()
            messages.success(request, "Successfully marked your attendance!")  
            return redirect('registration')  
    else:
        form = RegistrationForm()

    return render(request, 'registration_page.html', {'form': form})


