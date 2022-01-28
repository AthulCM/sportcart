from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from accounts import views
urlpatterns = [

    path('register/',views.register,name='register'),
    path('login/', views.login,name='login')

]