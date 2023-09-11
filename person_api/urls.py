from unicodedata import name
from django.urls import path
from . import views
#from .views import PersonApi


urlpatterns = [
    path('', views.person_list, name='person_list'),
    path('user_id/', views.person_detail, name='person_detail')
]