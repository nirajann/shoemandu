from django.urls import path

from . import views

urlpatterns = [
    path('adminmanage', views.adminmanage , name='adminmanage'),
    path('account', views.account , name='account'),
    path('orders', views.orders , name='orders'),
    path('productstore', views.productstore , name='productstore'),
    path('category', views.category , name='category'),
    path('editproduct/<int:pk>', views.editproduct , name='editproduct'),
    path('updateproduct/<int:pk>', views.updateproduct , name='updateproduct'),
]