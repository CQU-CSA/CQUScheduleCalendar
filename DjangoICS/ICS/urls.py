from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('get/',views.get, name='get'),
    path('download/',views.download,name='download'),
    path('api/<str:id>',views.api,name='api'),
]