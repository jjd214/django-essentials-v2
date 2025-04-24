from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Class base view
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = { 'date': datetime.now() }

class AuthorizeView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorize.html"
    # redirect
    login_url = "/admin"

# Create your views here.
# def home(request):
#     return render(request, 'home/welcome.html', { 'date': datetime.now })

# @login_required(login_url='/admin')
# def authorize(request):
#     return render(request, 'home/authorize.html', {})