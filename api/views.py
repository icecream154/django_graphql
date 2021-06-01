from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from project_config import PROJECT_ROOT


def index(request):
    html = None
    try:
        with open(PROJECT_ROOT + '/api/htmls/index.html', 'r') as f:
            html = f.read()
    except Exception as e:
        print(e)

    if not html:
        html = u'对不起加载出错了'
    return HttpResponse(html)


def java(request):
    html = None
    try:
        with open(PROJECT_ROOT + '/api/htmls/java.html', 'r') as f:
            html = f.read()
    except Exception as e:
        print(e)

    if not html:
        html = u'对不起加载出错了'
    return HttpResponse(html)


def graphql(request):
    html = None
    try:
        with open(PROJECT_ROOT + '/api/htmls/graphql.html', 'r') as f:
            html = f.read()
    except Exception as e:
        print(e)

    if not html:
        html = u'对不起加载出错了'
    return HttpResponse(html)