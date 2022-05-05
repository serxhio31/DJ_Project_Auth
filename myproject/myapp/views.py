from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def index(request):
    # context ={
    #     'name': 'sergio',
    #     'age':30,
    #     'nationality':'albanian'
    # }
    # feature1=Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.is_true = True
    # feature1.details = 'Our service is very quick'
    #
    # feature2=Feature()
    # feature2.id = 1
    # feature2.name = 'Reliable'
    # feature2.is_true = True
    # feature2.details = 'Our service is very reliable'
    #
    # feature3=Feature()
    # feature3.id = 2
    # feature3.name = 'Easy to use'
    # feature3.is_true = False
    # feature3.details = 'Our service is easy to use'
    #
    # feature4=Feature()
    # feature4.id = 3
    # feature4.name = 'Affordable'
    # feature4.is_true = True
    # feature4.details = 'Our service is very affordable'

    # return render(request, 'index.html', {'feature1': feature1 , 'feature2': feature2 , 'feature3': feature3 , 'feature4': feature4})
    # features =[feature1 ,feature2 , feature3 , feature4]
    features = Feature.objects.all()
    return render(request ,'index.html',{'features': features})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
#kontrollojme nese emaili eshte i njejte me repeated one dhe nese emaili ekziston me pare ne databaze
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password is not the same!')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username =request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username ,password=password)
#kontrollojme nese useri ekziston ne databaze apo jo
        if user is not None:
            auth.login(request,user)
            return redirect('/index')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')

    else:
        return render(request ,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/index')

def counter(request):
    text = request.POST['text']
    amount_of_words=len(text.split())
    return render(request,'counter.html',{'amount' : amount_of_words})

def static(request):
    return render(request, 'home.html')

