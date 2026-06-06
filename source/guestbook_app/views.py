from django.shortcuts import render, redirect, get_object_or_404
from guestbook_app.models import Entry
from guestbook_app.forms import EntryForm


def entry_list(request):
    entries = Entry.objects.filter(status='active')
    context = {'entries': entries}
    return render(request, 'guestbook_app/entry_list.html', context)


def entry_add(request):
    form = EntryForm()
    if request.method == 'GET':
        return render(request, 'guestbook_app/entry_add.html', {'form': form})
    elif request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
        return render(request, 'guestbook_app/entry_add.html', {'form': form})


def entry_edit(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    form = EntryForm(instance=entry)
    if request.method == 'GET':
        return render(request, 'guestbook_app/entry_edit.html', {'form': form, 'entry': entry})
    elif request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
        return render(request, 'guestbook_app/entry_edit.html', {'form': form, 'entry': entry})