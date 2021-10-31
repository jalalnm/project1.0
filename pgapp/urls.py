from django.urls import path
from . import views
urlpatterns=[
    path('project1',views.ntrends ,name='project1'),
    path('home',views.page1 ,name='home'),
    path('form2',views.page2 ,name='form2')
]