from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Journal
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = request.user
        journals = Journal.objects.filter(user=request.user)
        return render(request, 'home.html', {'user': user, 'journals' : journals})
    else:
        return render(request,'index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid username or password')
        return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Account created successfully!')
            login(request, user)
            return redirect('index')
        else:
            form.add_error(None, 'Invalid form data')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')

def journal_view(request):
    if request.method == 'POST':
        date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
        heading = request.POST['heading']
        entry = request.POST['entry']
        journal = Journal.objects.create(date=date, heading=heading, entry=entry, user=request.user)
        journal.save()
        return redirect('index')
    else:
        return render(request, 'journal.html')

def journal_detail(request, pk):
    journal = get_object_or_404(Journal,pk=pk,user=request.user)
    return render(request, 'view_journal.html', {'journal' : journal})

def journal_delete(request, pk):
    journal = get_object_or_404(Journal,pk=pk,user=request.user)
    journal.delete()
    return redirect('index')

def journal_edit(request, pk):
    journal = get_object_or_404(Journal,pk=pk,user=request.user)
    if request.method == 'POST':
        date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
        heading = request.POST['heading']
        entry = request.POST['entry']
        journal.date = date
        journal.heading = heading
        journal.entry = entry
        journal.save()
        return redirect('index')
    else:
        return render(request, 'edit_journal.html', {'journal' : journal})
