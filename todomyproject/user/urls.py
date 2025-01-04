from django.urls import path
from . import views

urlpatterns = [
    path('',views.register),
    path('1',views.log_in,name='login'),
    path('2',views.index),
    path('3',views.log_out),

]