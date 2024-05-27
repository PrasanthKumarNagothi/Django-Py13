from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homefeed'),
    path('upload', views.upload, name='upload'),
]
