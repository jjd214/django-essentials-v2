from django.urls import path
from . import views

urlpatterns = [
    # Class base view
    path('', views.HomeView.as_view()),
    # path('', views.home),
    
    path('authorize', views.AuthorizeView.as_view()),
    # path('authorize', views.authorize),
]
