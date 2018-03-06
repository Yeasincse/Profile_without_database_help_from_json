import urllib.request
import json
from django.shortcuts import render,redirect
from django.contrib.auth import  logout, login
from django.contrib.auth.decorators import login_required
login=False  #flag variable for checking

# Checking user authentication
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #user = authenticate('user'=username, 'user'=password)
        if username == 'user' and password == 'user':
            global login
            login = True
            return redirect('profile')
        else:
            return render(request, 'registration/login.html', {'error_message': 'Username or Password Invalid login'})
    return render(request, 'registration/login.html')


#@login_required
# user logout process method
def logout_user(request):
    global login
    if login == True:
        logout(request)
        login = False
        return redirect('login_user')


#@login_required
# user profile system
def profile(request):
    global login
    if login == True:
        user_login=True
        geourl = "https://randomuser.me/api/"
        response = urllib.request.urlopen(geourl)
        content = response.read()
        data = json.loads(content.decode("utf8"))
        return render(request, "registration/profile.html", {"data": data,"user_login":user_login})
    else:
        return redirect('login_user')
