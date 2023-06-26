from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',home),
    path('add/',post_employee),
    path('update/<int:id>/',update_employee),
    path('delete/<int:id>',delete_employee)
]