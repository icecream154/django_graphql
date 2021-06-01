from django.urls import path

from api.views import *

urlpatterns = [
    path('java_notes', java, name='java'),
    path('graphql_notes', graphql, name='java'),
    path('', index, name='index')
]