from django.shortcuts import render, get_object_or_404
from .models import Project, Tag

# A view is a function called when going to a specific root
def home(request):
    projects = Project.objects.all() # uses ORM from django, get all made projects
    tags = Tag.objects.all()
    return render(request, "home.html", {"projects": projects, "tags": tags})

def contact(request):
    return render(request, "contact.html")

def project(request, id):
    project = get_object_or_404(Project, pk=id) # "Look for this model that contains this key"
    return render(request, "project.html", {"project": project})