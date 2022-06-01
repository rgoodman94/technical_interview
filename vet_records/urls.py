from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>', views.Cat_Record_Controller.as_view()),
    path('', views.Cat_Record_Controller.as_view())
]