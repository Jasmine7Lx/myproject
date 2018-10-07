# coding=utf-8
from django.shortcuts import render,get_list_or_404,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
#from .models import superuser
from django.template import RequestContext

# Create your views here.
'''
def list(request):
    user_list = superuser.objects.all()
    context = {'user_list': user_list}
    return render(request, 'report/index.html', context)



def loginVerify(request):  #登录信息提交验证
    if request.method == 'POST':
        return HttpResponse()
    #login_state = {}

'''
def login(request):
    return render(request, 'login.html')
    
def w_report(request):
    pass

def bug_list(request):
    pass

def logout(request):
    pass
