from . import views
from django.urls import path
app_name = 'portail'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/',views.post_list, name='posts'),
    path('<slug:post>/',views.post_detail,name='post_detail'),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_tag'),
] 
