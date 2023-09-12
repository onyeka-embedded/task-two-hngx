from unicodedata import name
from django.urls import path
from . import views
#from .views import PersonAp


urlpatterns = [
    path('api', views.person_list, name='person_list'),
    path('api/<str:pk>', views.person_detail, name='person_detail')
]