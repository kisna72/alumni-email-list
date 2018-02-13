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
from django.urls import path , include
from . import views
from django.contrib.auth import views as authviews

login_template = "basicauth/login.html"
logout_template = "basicauth/logout_complete.html"
password_reset_template = "basicauth/password_reset.html"
password_reset_request_done_template = "basicauth/password_reset_done.html"
password_reset_confirm_template = "basicauth/password_reset_confirm.html"
password_reset_completed_template = "basicauth/password_reset_complete.html"

urlpatterns = [
    path('signup/',views.signup, name="signup"),

	path('login/', authviews.LoginView.as_view(template_name=login_template), name='login'),
	path('logoutconfirm/', views.logoutconfirm, name='logoutconfirm'),#Todo...
	path('logout/', authviews.LogoutView.as_view(template_name=logout_template), name='logout'),
	#path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
 	#path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
 	path('password_reset/', authviews.PasswordResetView.as_view(template_name=password_reset_template), name='password_reset'),
    path('password_reset/done/', authviews.PasswordResetDoneView.as_view(template_name=password_reset_request_done_template), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', authviews.PasswordResetConfirmView.as_view(template_name=password_reset_confirm_template), name='password_reset_confirm'),
    path('reset/done/', authviews.PasswordResetCompleteView.as_view(template_name=password_reset_completed_template), name='password_reset_complete'),

    path('', include('django.contrib.auth.urls')),
]


# From django.contrib.auth.urls: 
# from django.contrib.auth import views
# from django.urls import path

# urlpatterns = [
#     path('login/', views.LoginView.as_view(), name='login'),
#     path('logout/', views.LogoutView.as_view(), name='logout'),

#     path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
#     path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

#     path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
#     path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]