from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myproducts/',views.ProductsByUserListView.as_view(), name='my-products'),
    path('users/',views.UserListView.as_view(), name="users"),
]
