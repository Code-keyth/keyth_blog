# -*- coding:UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import requests
import uuid
from lxml import etree
import os,re
from PIL import Image
import time
import hashlib

course_xpath='//*[@id="courseSelect"]'
post_action="http://218.198.176.244/etses/security/loginAction_uniteLogin.action"
img_url="http://218.198.176.244/etses/security/loginAction_loadValidateCode.action"
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index/pj.html', context)
def getImage(url,cookie):
	path = "static/images/{}.jpg".format(uuid.uuid1())
	data = requests.get(url,cookies=cookie)
	fh = open(path, 'wb')
	fh.write(data.content) 
	fh.close()
	return path
def start(request):
    if not os.path.isdir('static/images'):
        os.makedirs('static/images/')
    global cookie
    cookie=requests.utils.dict_from_cookiejar((requests.get('http://218.198.176.244/etses/face/userLogin.jsp')).cookies)

    path=getImage(img_url,cookie)
    ctx ={}
    ctx['path']='/'+path
    if request.POST:
        ctx['username'] = request.POST['username']
        ctx['password'] = request.POST['password']
        ctx['uvc'] = request.POST['uvc']
    
    return render(request, "index/pj.html", ctx)

def post(request):
    global cookie
    ctx ={}
    md5 = hashlib.md5()
    if request.POST:
        ctx['username'] = request.POST['username']
        ctx['password'] = request.POST['password']
        ctx['uvc'] = request.POST['uvc']
    if ctx['password']:
        md5.update(bytes(ctx['password'], encoding='utf8'))
    else:
        md5.update(bytes('123456', encoding='utf8'))
    password = md5.hexdigest()
    data={
		"username":ctx['username'],
		"password":password,
		"uvc":ctx['uvc'],
		"identity":"1",}
    aaa=requests.post(post_action,cookies=cookie,data=data)

    index_request = requests.get('http://218.198.176.244/etses/student/studentEvalAction_evaTeacher.action',cookies=cookie).text
    Course,Teacher=getCourse(etree.HTML(index_request).xpath(course_xpath)[0],cookie)
    sum=int(len(Teacher))-1
    while(sum>-1):

  
        get="http://218.198.176.244/etses/student/studentEvalAction_validateAndSaveEval.action?stutotea.counid="
        +kcs[sum]+"&stutotea.teano="
        +ls_bianhao[sum]+"&eid=1000000017&weight=15&mark="
        +str(random.randint(4,5))+"&eid=1000000018&weight=10&mark="
        +str(random.randint(4,5))+"&eid=1000000019&weight=20&mark="
        +str(random.randint(4,5))+"&eid=1000000020&weight=15&mark="
        +str(random.randint(4,5))+"&eid=1000000021&weight=15&mark="
        +str(random.randint(4,5))+"&eid=1000000022&weight=10&mark=4&eid=1000000023&weight=10&mark="
        +str(random.randint(4,5))+"&eid=1000000024&weight=5&mark="
        +str(random.randint(4,5))+"&stutotea.othcomments="
        aaa=requests.post(get,cookies=cookie)
        print(str(ls_bianhao[sum]))
        sum=sum-1
    ctx['qq']=index_request

    return render(request, "index/pj.html", ctx)

def getCourse(kechengs,cookie):
    Course=[]
    Teacher=[]
    for kecheng in kechengs:
        if len(kecheng.get('value'))>2:
            Course.append(kecheng.get('value'))
    for value in Course:
        data={'couno':value}
        ls=requests.post('http://218.198.176.244/etses/student/studentEvalAction_getTeachByCountId.action',cookies=cookie,data=data)
        ls_arr=(ls.content).split('["')
        for i in range(1,len(ls_arr)):
            Teacher.append(((ls_arr[i]).split('",'))[0])
    return (Course,Teacher)
    