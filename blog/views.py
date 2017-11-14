from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index/index.html')
def blog(request):
    return render(request, 'index/blog1.html')
def skill(request):
    return render(request, 'index/skill.html')