from django.shortcuts import render
from Admin.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):

    return render(request, 'index/index.html')
def blog(request):
    blogs_list=Blog.objects.all()
    paginator = Paginator(blogs_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request, 'index/blog1.html',{'blogs':blogs})
def skill(request):
    skill_type=Skill_type.objects.all()
    if request.GET:
        if request.GET['type']:
            skill_type=Skill_type.objects.filter(id=request.GET['type'])
    return render(request, 'index/skill.html',{'skill_type':skill_type})