from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    # path('notes/<int:id>', views.detail),
    # path('popular', views.popular_notes),

    # DetailView expeect pk not id
    path('notes', views.ListView.as_view(), name='notes.list'),
    path('notes/<int:pk>', views.DetailView.as_view(), name='notes.details'),
    path('notes/popular', views.PopularNotesView.as_view()),
    path('notes/create', views.NotesCreateView.as_view(), name='notes.create'),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name='notes.update'),
]