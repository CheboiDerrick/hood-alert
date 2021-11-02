from django.urls import path,include
from mainapp import views



urlpatterns = [
    path('',views.home,name='home'),
    path("profile/", views.profile, name="profile"), # profile page
    path("profile/update/", views.update_profile, name="update_profile"), # profile update page
    path("post/save/", views.create_post, name="save_post"), # save post
]