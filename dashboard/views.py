from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Project


@login_required(login_url='/admin/')  # Filhal login ke liye Django admin use karenge
def dashboard_home(request):
  projects = Project.objects.filter(owner=request.user)
  context = {'projects': projects}
  return render(request, 'dashboard/home.html', context)