from django.shortcuts import render
from .models import Notes

# Create your views here.
def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_lists.html', { 'notes': all_notes })