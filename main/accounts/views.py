from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:  # daca a completat tot la login
            auth.login(request, user)
            return redirect('/')  # il logheaza si l trimite in home
        else:
            messages.error(request, 'invaild credentials') # daca nu sunt corecte ii da eroare
            return redirect('login')  # si l pune sa bage alte date
    else:
        return render(request, 'login.html') 
        

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']  # astea s toate campurile la register
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2: # daca a bagat parola corect de 2 ori

            if User.objects.filter(username=username).exists():   # daca username este in db
                messages.error(request, 'Username Taken')  # ii da eroare si il pune sa bage altul
                return redirect('register')

            elif User.objects.filter(email=email).exists(): # daca emailul este in db
                messages.error(request, 'Email Taken') # ii da eroare si il pune sa bage altul
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name) # campurile se inregistreaza in db
                user.save() # se salveaza userul
                print('user created')
                return redirect('login')  # s-a inregistrat si e gata de login

        else:
            messages.error(request, "Password not matching.")  # daca nu a bagat aceeasi parola in register da eroare
            return redirect('register') # si il pune sa bage aceeasi parola ca sa creeze contul

        return redirect('/')
    else:
        return render(request, 'register.html') 


def logout(request):
    auth.logout(request)
    return redirect("/")
