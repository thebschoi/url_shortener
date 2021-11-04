from django.urls import path
from . import views

app_name = 'my_url'
urlpatterns = [
    path('my_url/', views.my_url, name='my_url'),
    path('<new_url>/', views.original, name='original'),
    path('', views.web_open, name='web_open'),
]