from django.urls import path

from personal_task_manager.common import views

urlpatterns = [
    path('', views.index, name='index'),

]