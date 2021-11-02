from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainapp import views




urlpatterns = [
    path('',views.home,name='home'),
    path("profile/", views.profile, name="profile"),
    path("profile/update/", views.update_profile, name="update_profile"),
    path("post/save/", views.create_post, name="save_post"), 
    path("business/create/", views.create_business, name="create_business"),
    path("contact/create/", views.create_contact, name="create_contact"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)