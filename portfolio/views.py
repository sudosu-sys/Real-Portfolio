from django.shortcuts import render
from .models import Project
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    context = {
        'projects': Project.objects.prefetch_related('images', 'technologies')
    }
    return render(request, "portfolio/index.html", context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "portfolio/project_detail.html", {'project': project})