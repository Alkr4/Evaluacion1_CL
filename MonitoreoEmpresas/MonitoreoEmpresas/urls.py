"""
URL configuration for MonitoreoEmpresas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from dispositivos.views import dashboard, device_list, device_detail, alert_list, measurement_list
from usuarios.views import login, register, logout, password_reset, password_reset_confirmed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('', dashboard, name='dashboard'),
    path('devices/', device_list, name='device_list'),
    path('devices/<int:device_id>/', device_detail, name='device_detail'),
    path('logout/', logout, name='logout'),
    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset_confirmed/', password_reset_confirmed, name='password_reset_confirmed'),
    path('alerts/', alert_list, name='alert_list'),
    path('measurements/', measurement_list, name='measurement_list'),
]
