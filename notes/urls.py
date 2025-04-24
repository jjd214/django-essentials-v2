from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    # path('notes/<int:id>', views.detail),
    # DetailView expeect pk not id
    path('notes/<int:pk>', views.DetailView.as_view()),
    path('notes', views.ListView.as_view())
]