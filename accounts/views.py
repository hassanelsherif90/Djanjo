from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
# Create your views here.
def login_viwe(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        user = authenticate(request, username = username,password = password)
        if user is None:
            context = {"error": "Invalide username or password"}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html', {})


def logout_viwe(request):
    return render(request, 'accounts/login.html', {})

