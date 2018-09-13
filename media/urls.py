from django.urls import path

from . import views

urlpatterns = [
    # path('', views.QustionList.as_view()),
    path('upload', views.upload),
    path('<int:id>/comments', views.comments),
    path('<int:id>/likes', views.likes)
]