from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('emaillist_home')
    else:
        from django.core.mail import send_mail

        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

        form = SignUpForm()
    return render(request, 'basicauth/signup.html', {'form': form})

def logoutconfirm(request):
    if request.method == "POST":
        pass
    else:
        pass
    return render(request, "basicauth/logoutconfirm.html")