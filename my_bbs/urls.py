
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'my_bbs'

urlpatterns = [
    path('list/', views.p_list, name='list'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),

    path('create/', views.p_create, name='create'),


    path('<int:board_id>/delete/', views.p_delete, name='delete'),
    path('<int:board_id>/update/', views.p_update, name='update'),
    path('<int:board_id>/comment/', views.c_list, name='comment'),
    path('<int:board_id>/c_create/', views.c_create, name='c_create'),
    path('<int:ct_id>/c_delete/', views.c_delete, name='c_delete'),

]
