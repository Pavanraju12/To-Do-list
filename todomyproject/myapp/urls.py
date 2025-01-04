from django.urls import path
from . import views

urlpatterns = [
   
    path('4', views.home, name='home'),
    path('todolist/', views.todolist, name='todolist'),
    path('history/', views.history, name='history'),
    path('contact/', views.contact, name='contact'),
    path('mark_as_reviewed/<int:pk>/', views.mark_as_reviewed, name='mark_as_reviewed'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),
]
