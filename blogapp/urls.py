from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
  # path('',views.demo,name='demo'),
  path('register/',views.register,name='user.register'),
  path('login/',views.user_login,name='user.login'),
  path('dashboard/',views.user_dashboard,name='user.dashboard'),
  path('logout/',views.user_logout,name='user.logout'),
#    path('edit/<int:post_id>/',views.user_edit,name='post_edit'),
#    path('show/<int:post_id>/',views.user_show,name='user_show'),

    #CRUD
  path('posts/',views.post_index,name='post_index'),
  path('edit/<int:post_id>/',views.post_edit,name='post_edit'),
  path('show/<int:post_id>/',views.post_show,name='post_show'),
  path('create/',views.post_create,name='post_create'),
  path('update/',views.post_update,name='post_update'),
  path('delete/<int:post_id>/',views.post_delete,name='post_delete'),

    #Test
    path('test/',views.test,name='test'),
]
