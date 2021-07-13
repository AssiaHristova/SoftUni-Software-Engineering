from django.shortcuts import render, redirect

from notes.note_app.forms import CreateNoteForm, DeleteNoteForm
from notes.note_app.models import Note
from notes.profile_app.models import Profile


def home_page(request):
    profile = Profile.objects.first()
    if not profile:
        return redirect('create_profile')
    else:
        notes = Note.objects.all()
        context = {'notes': notes}
        return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'GET':
        form = CreateNoteForm()
        context = {'form': form}
        return render(request, 'note-create.html', context)
    form = CreateNoteForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home page')
    context = {'form': form}
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        form = CreateNoteForm(instance=note)
        context = {'form': form}
        return render(request, 'note-edit.html', context)
    form = CreateNoteForm(request.POST, instance=note)
    if form.is_valid():
        form.save()
        return redirect('home page')
    context = {'form': form}
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteNoteForm(instance=note)
        context = {'form': form}
        return render(request, 'note-delete.html', context)
    note.delete()
    return redirect('home page')


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {'note': note}
    return render(request, 'note-details.html', context)
