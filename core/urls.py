"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token
from . views import MyTokenObtainPairView
from  rest_framework.authentication import TokenAuthentication #For token Authentication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/firstapp/',include('firstapp.urls')),

    path('api/login-api/',obtain_auth_token), #For token Authentication
    path('api/token/',MyTokenObtainPairView.as_view()),#For simple jwt Authentication
    # path('api/token/',TokenObtainPairView.as_view()),#For simple jwt Authentication
    path('api/token/refresh/',TokenRefreshView.as_view()),#For simple jwt Authentication

]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)