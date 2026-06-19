from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Note


def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        return redirect('home')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('home')

    return render(request, 'register.html')


@login_required
def dashboard(request):
    notes = Note.objects.filter(user=request.user)
    search = request.GET.get('search')
    if search:
        notes = notes.filter(title__icontains=search)

    category = request.GET.get('category')
    if category:
        notes = notes.filter(category=category)

    recent_notes = Note.objects.filter(user=request.user).order_by('-updated_at')[:5]
    context = {
        'notes': notes,
        'recent_notes': recent_notes,
        'search': search,
        'category': category,
    }
    return render(request, 'dashboard.html', context)


@login_required
def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')

        Note.objects.create(
            user=request.user,
            title=title,
            content=content,
            category=category,
        )
        return redirect('dashboard')

    return render(request, 'create_note.html')


@login_required
def edit_note(request, id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.category = request.POST.get('category')
        note.save()
        return redirect('dashboard')

    return render(request, 'edit_note.html', {'note': note})


@login_required
def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('dashboard')


def logout_user(request):
    logout(request)
    return redirect('home')