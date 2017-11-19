from django.shortcuts import render
from Admin.models import *
import json
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    return render(request, 'index/index.html')
def blog(request):
    blogs_list=Blog.objects.filter(state=1)
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
    skill_list=Skill.objects.filter(state=1)
    paginator = Paginator(skill_list, 8) # Show 25 contacts per page
    page = request.GET.get('page')
    type_ids=arrays(Skill_type,'id')
    try:
        if int(request.GET['type']) in type_ids:
            skills=Skill.objects.filter(classify=request.GET['type'],state=1)
            paginator = Paginator(skills, 8) # Show 25 contacts per page
            page = request.GET.get('page')
    except:
        try:
            skills = paginator.page(page)
        except PageNotAnInteger:
            skills = paginator.page(1)
        except EmptyPage:
            skills = paginator.page(paginator.num_pages)
        
    return render(request, 'index/skill.html',{'skill_type':skill_type,'skills':skills})
def post(request):

    try:
        Reply1=Reply.objects.filter(tid=0,articleid=request.GET['id'])
        Reply2=Reply.objects.filter(tid=1,articleid=request.GET['id'])
        if request.path == '/blog/post/':
            ids=arrays(Blog,'id')
            url='/blog/'
            if int(request.GET['id']) in ids:
                content=Blog.objects.get(id=request.GET['id'])
                
                Blog.objects.filter(id=request.GET['id']).update(clicks=content.clicks+1)
            else:
                return HttpResponse(alertjs('该文章不存在','index'))
        elif request.path == '/skill/post/':
            ids=arrays(Skill,'id')
            if int(request.GET['id']) in ids:
                content=Skill.objects.get(id=request.GET['id'])
                Skill.objects.filter(id=request.GET['id']).update(clicks=content.clicks+1)
                url='/skill/'
            else:
                return HttpResponse(alertjs('该文章不存在','index'))
    except:
        return HttpResponse(alertjs('该文章不存在','index'))
    return render(request, 'index/post.html',{'content':content,'reply1':Reply1,'reply2':Reply2})



def reply(request):
    try:
        if request.is_ajax():
            postdata=request.GET
            Reply(username=postdata['username'],content=postdata['content'],email=postdata['email'],fid=postdata['fid'],tid=postdata['tid'],articleid=postdata['articleid'],).save()
            return HttpResponse('评论成功！') 
    except:
       return HttpResponse('评论失败！')
def pingjiao(string,url):
    return '<script type="text/javascript">alert("{}"); window.location="{}";\
            var index = parent.layer.getFrameIndex(window.name);\
            parent.layer.close(index);\
            </script>'.format(string,url)
def arrays(obj,filter):
    ids=[]
    for id in obj.objects.values_list(filter,flat=True):
        ids.append(id)
    return ids
def alertjs(string,url):
    return '<script type="text/javascript">alert("{}"); window.location="{}";\
            var index = parent.layer.getFrameIndex(window.name);\
            parent.layer.close(index);\
            </script>'.format(string,url)