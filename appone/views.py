# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.models import Group
from appone.models import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from add_assets.serializers import *
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

def getBaseAssets():
    try:
        groupList = Group.objects.all()
    except:
        groupList = []
    return {"group":groupList}



@login_required(login_url='/login')
@permission_required('add_assets.can_add_assets',login_url='/noperm/')
def assets_add(request):
    if request.method == 'GET':
        return render_to_response('assets_add.html',{"user":request.user,
                                                            "baseAssets":getBaseAssets()})



@csrf_exempt
def login(request):
    if request.session.get('username') is not None:
        return HttpResponseRedirect('/',{"user":request.user})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user and user.is_active:
            auth.login(request,user)
            request.session['username'] = username
            return HttpResponseRedirect('/user/center/',{"user":request.user})
        else:
            if request.method == 'POST':
                return render_to_response('login.html',{"login_error_info":"用户名不存在，或者密码错误!"})
            else:
                return render_to_response('login.html')



@login_required()
def user_center(request):
    if request.method == 'GET':
        return render_to_response('user_center.html',{"user":request.user})


@login_required(login_url='/login')
def index(request):
    return render_to_response('index.html',{"user":request.user})





@api_view(['GET', 'POST' ])
@permission_required('add_assets.can_add_server_assets',raise_exception=True)
def asset_server_list(request,format=None):
    """
    List all order, or create a server assets order.
    """

    if request.method == 'GET':
        snippets = Server_Assets.objects.all()
        serializer = ServerSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if(request.data.get('data')):
            data =  request.data.get('data')
        else:
            data = request.data
        serializer = ServerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)