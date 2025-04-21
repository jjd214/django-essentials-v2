from django.shortcuts import render
from .models import Notes
from django.http import Http404

# Create your views here.
def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_lists.html', { 'notes': all_notes })

def detail(request, id):
    try:
        note = Notes.objects.get(pk=id)
    except Notes.DoesNotExist:
        raise Http404("Note id does not exist.")
    return render(request, 'notes/notes_details.html', { 'note': note })