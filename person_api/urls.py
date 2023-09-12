from unicodedata import name
from django.urls import path
from . import views
#from .views import PersonAp


urlpatterns = [
    path('', views.person_list, name='person_list'),
    path('/<str:pk>', views.person_detail, name='person_detail')
]