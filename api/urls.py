from django.urls import path

from api.views import *

urlpatterns = [
    path('java', java, name='java'),
    path('graphql', graphql, name='java'),
    path('', index, name='index')
]