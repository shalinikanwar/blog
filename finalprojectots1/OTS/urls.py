from django.urls import path
from .views import *
urlpatterns = [
    path('new-blog/',newblog),
    path('save-blog/',saveblog),
    path('view-blog/',viewblog),
    path('edit-blog/',editblog),
    path('edit-save-blog/',editsaveblog),
    path('delete-blog/',deleteblog),
    path('signup/',signup),
    path('save-user/',saveUser),
    path('login/',login),
    path('login-validation/',loginValidation),
    path('home/',home),
    path('logout/',logout),
    path('start-blog/',startblog),
    
    
    
]