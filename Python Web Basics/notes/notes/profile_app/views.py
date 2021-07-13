from django.shortcuts import render, redirect

from notes.note_app.models import Note
from notes.profile_app.forms import ProfileForm
from notes.profile_app.models import Profile


def create_profile(request):
    if request.method == 'GET':
        form = ProfileForm()
        context = {'form': form}
        return render(request, 'home-no-profile.html', context)

    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home page')
    context = {'form': form}
    return render(request, 'home-no-profile.html', context)


def profile_page(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    if request.method == 'GET':
        notes_count = len(notes)
        context = {'profile': profile,
                   'notes_count': notes_count,
                }
        return render(request, 'profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    notes.delete()
    profile.delete()
    return redirect('home page')
