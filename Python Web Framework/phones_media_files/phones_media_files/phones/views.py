from django.shortcuts import render, redirect

from phones_media_files.phones.forms import PhoneForm
from phones_media_files.phones.models import Phone


def index(request):
    phones = Phone.objects.all()
    for phone in phones:
        phone.selected_image = phone.phoneimage_set.filter(is_selected=True).first()
    context = {'phones': phones}
    return render(request, 'index.html', context)


def create_phone(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
    form = PhoneForm()
    context = {'form': form}
    return render(request, 'create_phone.html', context)
