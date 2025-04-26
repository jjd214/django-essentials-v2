from django.shortcuts import render
from .models import Notes
from django.http import Http404
# TemplateView and ListView, DetailView is different
# ListView already make the query
from django.views.generic import ListView, DetailView, TemplateView, CreateView

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url = '/smart/notes'
    template_name = 'notes/notes_form.html'

class ListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_lists.html"

class DetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_details.html"

class PopularNotesView(ListView):
    model = Notes
    context_object_name = "popular_notes"
    template_name = "notes/popular_notes.html"
    queryset = Notes.objects.filter(likes__gt=1)

# Solution using TemplateView
# class PopularNotesView(TemplateView):
#     template_name = "notes/popular_notes.html"
#     extra_context = { 'popular_notes': Notes.objects.filter(likes__gt=1) }

# Create your views here.
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_lists.html', { 'notes': all_notes })

# def detail(request, id):
#     try:
#         note = Notes.objects.get(pk=id)
#     except Notes.DoesNotExist:
#         raise Http404("Note id does not exist.")
#     return render(request, 'notes/notes_details.html', { 'note': note })

# def popular_notes(request):
#     popular_notes = Notes.objects.filter(likes__gt=1)
#     return render(request, 'notes/popular_notes.html', { 'popular_notes': popular_notes })
