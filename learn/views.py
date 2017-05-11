from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    # return HttpResponse(u"欢迎光临 自强学堂!")
    #一、字符串
    # string = '学习建站！'
    # return render(request, 'learn/home.html',{'string':string})
    #二、数组
    # TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    # return render(request, 'learn/home.html',{'TutorialList':TutorialList})
    #三、字典
    # info_dict = {'site': '自强学堂', 'content': '各种IT技术教程'}
    # return render(request, 'learn/home.html',{'info_dict':info_dict})
    List = map(str,range(100)) #长度100 的数组
    return render(request, 'learn/home.html',{'List':List})



def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2',args=(a, b))
    )
