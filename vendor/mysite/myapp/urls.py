from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name="index"),
    path('product/<int:id>/',views.detail_view,name="product"),
    path('create/',views.create_product,name="create"),
    path('edit/<int:id>/',views.product_edit,name="edit"),
    path('delete/<int:id>/',views.product_delete,name="delete"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('register/',views.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name='myapp/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='myapp/logout.html'),name="logout"),
    path('invalid/',views.invalid,name="invalid"),


]
