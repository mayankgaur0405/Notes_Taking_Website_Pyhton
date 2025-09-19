from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from .models import Note
from .forms import NoteForm


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('notes:note_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('notes:note_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')


@login_required
def note_list(request):
    notes = Note.objects.filter(author=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes})


@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk, author=request.user)
    return render(request, 'notes/note_detail.html', {'note': note})


@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            messages.success(request, 'Note created successfully!')
            return redirect('notes:note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Create Note'})


@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, author=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully!')
            return redirect('notes:note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Update Note'})


@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, author=request.user)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted successfully!')
        return redirect('notes:note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
