from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from career.models import Register
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def loginuser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect("/home")
        
        else:
            return render(request, 'login.html')
        
    return render(request, 'login.html')
def register(request):

    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        # gender = request.POST['gender']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1== password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username is already taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Email is already registered')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=name)
                user.save()

                register = Register(username=username, name=name, email=email, pswd=password1,phone=contact )
                register.save()
                messages.success(request, 'User register succesfully')
                print('user created')
                return redirect('/login')
        else:
            messages.warning(request, "password is not matching")
            print('password not matching')
            return redirect('/register')

    else:
        return render(request, 'register.html')
    

@login_required(login_url='login')
def home(request):
    print(request.user)
    return render(request,'home.html')
    # return HttpResponse('this is home page')

def logoutUser(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login')
def profile(request):
    register = Register.objects.all()
    return render(request, 'profile.html',{'register': profile})


@login_required(login_url='login')
def explore(request):
    return render(request, 'explore_career.html')


@login_required(login_url='login')
def success(request):
    return render(request, 'success_story.html')


@login_required(login_url='login')
def career(request):
    return render(request, 'studyoption.html')


@login_required(login_url='login')
def goal(request):
    return render(request, 'setgoals.html')

@login_required(login_url='login')
def test(request):
    return render(request, 'test.html')