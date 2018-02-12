"""uno_email_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('',views.home, name="emaillist_home"),
    path('add_organization/',views.add_organization, name="organization_add"),
    path('org/<int:organization_pk>/', views.organization_detail, name='organization_detail'),
    #path('org/(?P<organization_pk>[\d]+)/$',views.organization_detail, name="organization_detail"),
    path('org/(?P<organization_pk>[\d]+)/edit/$',views.organization_detail, name="edit_organization"),
    path('org/(?P<organization_pk>[\d]+)/delete/$',views.organization_detail, name="delete_organization"),



]
