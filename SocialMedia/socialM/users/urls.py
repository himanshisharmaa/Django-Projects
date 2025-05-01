from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view
urlpatterns = [
    path("",index,name='home'),
    path("login/",user_login,name='login'),
    path("register/",register,name='register'),
    path("edit/",edit,name='edit'),
    path("logout/",auth_view.LogoutView.as_view(template_name="users/logout.html"),name='logout'),
    path("password-change/",auth_view.PasswordChangeView.as_view(template_name="users/password_change.html"),name='password_change'),
    path("password-change/done/",auth_view.LogoutView.as_view(template_name="users/password_change_done.html"),name='password_change_done'),
    path("password-reset/",auth_view.PasswordResetView.as_view(template_name="users/password_reset.html"),name='password_reset'),
    path("password-reset/done/",auth_view.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),name='password_reset_done'),
    path("reset/<uidb64>/<token>/",auth_view.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),name='password_reset_confirm'),
    path("reset/done/",auth_view.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),name='password_reset_complete'),

]
