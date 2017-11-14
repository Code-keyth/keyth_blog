from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'admin/index.html')
def blog_list(request):
    return render(request, 'admin/blog_list.html')
def blog_add(request):
    return render(request, 'admin/blog_add.html')
def skill_category(request):
    return render(request, 'admin/skill_category.html')
def skill_list(request):
    return render(request, 'admin/skill_list.html')

def welcome(request):
    return render(request, 'welcome.html')

def skill_lis111(request):
    print('1')
    return render(request, 'index.html')