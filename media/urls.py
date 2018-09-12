from django.urls import path

from . import views

urlpatterns = [
    # path('', views.QustionList.as_view()),
    path('upload', views.upload)
]