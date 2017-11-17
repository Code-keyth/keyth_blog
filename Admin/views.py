from django.shortcuts import render
from Admin.models import *
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'admin/index.html')
def blog_list(request):
    data = Blog.objects.all()
    return render(request, 'admin/blog_list.html',{'data':data})

def blog_add(request):
    if request.GET:
        ids=arrays(Blog,'id')
        if int(request.GET['id']) in ids:
            data=Blog.objects.get(id=request.GET['id'])
            return render(request, 'admin/blog_add.html',{'data':data})
    return render(request, 'admin/blog_add.html')
def blog_shenhe(request):
    if request.GET:
        print('11')
        ids=arrays(Blog,"id")
        if int(request.GET['id']) in ids:
            Blog.objects.filter(id=request.GET['id']).update(state=request.GET['state'])
            return HttpResponse(True)
    return HttpResponse(False)
####处理博文添加修改
def blog_add_c(request):
    if request.POST:
        data=request.POST
        if request.GET['id']:
            if request.FILES.get('thumbnail'):
                state=Blog.objects.get(id=request.GET['id'])
                state.thumbnail=request.FILES.get('thumbnail')
                state.save()
            Blog.objects.filter(id=request.GET['id']).update(updatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),title=data['title'],label=data['label'],outline=data['outline'],autor=data['autor'],editorValue=data['editorValue'])
        else :
            if request.FILES.get('thumbnail'):
                Blog(thumbnail=request.FILES.get('thumbnail'),title=data['title'],label=data['label'],outline=data['outline'],autor=data['autor'],editorValue=data['editorValue']).save()
            else:
                Blog(title=data['title'],label=data['label'],outline=data['outline'],autor=data['autor'],editorValue=data['editorValue']).save()


    return HttpResponse(alertjs('添加成功','blog_add'))

####博文删除
def blog_del(request):
    if request.GET['id']:
        Blog.objects.filter(id=request.GET['id']).delete()
        return HttpResponse(True)
    return HttpResponse(False)

def skill_category(request):
    skills=Skill_type.objects.all()
    ids=arrays(Skill_type,'id')
    if request.POST :
        if request.POST['name'] :
            if request.GET['id']:
                if int(request.GET['id']) in ids:
                    Skill_type.objects.filter(id=request.GET['id'],).update(name=request.POST['name'])
                    return HttpResponse(alertjs('修改成功！！','skill_category'))
            else :
                Skill_type(name = request.POST['name']).save()
                return HttpResponse(alertjs('添加成功！！','skill_category'))
    elif request.GET: 
        if  request.GET['id'] and int(request.GET['id']) in ids:
            skill=Skill_type.objects.get(id=request.GET['id'])
            return render(request, 'admin/skill_category.html',{"skill":skill,"skills":skills})
    return render(request, 'admin/skill_category.html',{"skills":skills})

def skill_add(request):
    ids=arrays(Skill,'id')
    if request.GET:
        #打开新增界面
        if request.GET['id']:
            #修改技术贴
            if int(request.GET['id']) in ids :
                if request.POST:
                    if request.FILES.get('thumbnail'):
                        state=Skill.objects.get(id=request.GET['id'])
                        state.thumbnail=request.FILES.get('thumbnail')
                        state.save()
                    data=request.POST
                    Skill.objects.filter(id=request.GET['id']).update(title=data['title'],classify=data['classify'],label=data['label'],outline=data['outline'],autor=data['autor'],editorValue=data['editorValue'])
                    return HttpResponse(alertjs('技术贴修改成功！！','skill_list'))

                data=Skill.objects.get(id=request.GET['id'])
                return render(request, 'admin/skill_add.html',{'data':data})
            else:
                return HttpResponse(alertjs('非法操作！！','skill_list'))
        else:
            #新增技术贴
            if request.POST:
                data2=request.POST
                if request.FILES.get('thumbnail'):
                    Skill(thumbnail=request.FILES.get('thumbnail'),title=data2['title'],classify=data2['classify'],label=data2['label'],outline=data2['outline'],autor=data2['autor'],editorValue=data2['editorValue']).save()
                else:
                    Skill(title=data2['title'],classify=data2['classify'],label=data2['label'],outline=data2['outline'],autor=data2['autor'],editorValue=data2['editorValue']).save()
                return HttpResponse(alertjs('技术贴添加成功！！','skill_list'))
            else:
                return HttpResponse(alertjs('没有收到数据！！','skill_list'))
    return render(request, 'admin/skill_add.html',{'skill_types':Skill_type.objects.all()})

def skill_list(request):
    skills=Skill.objects.all()
    if request.GET:
        if request.GET['type']:
            skills=Skill.objects.filter(classify=request.GET['type'])

    return render(request, 'admin/skill_list.html',{'skill_types':Skill_type.objects.all(),'skills':skills})
def skill_del(request):
    if request.GET['id']:
        Skill.objects.filter(id=request.GET['id']).delete()
        return HttpResponse(True)
    return HttpResponse(False)
def skill_shenhe(request):
    if request.GET:
        print('11')
        ids=arrays(Skill,"id")
        if int(request.GET['id']) in ids:
            Skill.objects.filter(id=request.GET['id']).update(state=request.GET['state'])
            return HttpResponse(True)
    return HttpResponse(False)
def alertjs(string,url):
    return '<script type="text/javascript">alert("{}"); window.location="{}";\
            var index = parent.layer.getFrameIndex(window.name);\
            parent.layer.close(index);\
            </script>'.format(string,url)

def arrays(obj,filter):
    ids=[]
    for id in obj.objects.values_list(filter,flat=True):
        ids.append(id)
    return ids
    