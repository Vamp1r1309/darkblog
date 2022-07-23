from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('category/<slug:slug>', get_category, name='category')
]
