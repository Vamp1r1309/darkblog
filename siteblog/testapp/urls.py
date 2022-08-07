from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('', test, name='test'),
    path('rubric/<int:pk>', get_rubric, name='rubric')
]