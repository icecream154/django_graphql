from django.urls import path

from api.views import *

urlpatterns = [
    path('java_notes', java, name='java'),
    path('graphql_notes', graphql, name='java'),
    path('aop_notes', aop, name='aop'),
    path('', index, name='index')
]