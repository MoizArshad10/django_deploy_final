from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('' , views.member_list.as_view(), name='member_list'),
    path('create/' , views.create_member.as_view(), name='create_member'),
    path('update/<int:pk>' , views.update_member.as_view(), name='update_member'),
    path('delete/<int:pk>' , views.delete_member.as_view(), name='delete_member'),
]

