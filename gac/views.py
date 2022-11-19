from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from .models import Product
from django.contrib.auth.models import User

class ProductsByUserListView(LoginRequiredMixin,generic.ListView):
    model = Product
#    template_name = 'gac/product_list_user.html'
    def get_queryset(self):
        return Product.objects.filter(supplier=self.request.user)

class UserListView(PermissionRequiredMixin,generic.ListView):
    permission_required = "auth.view_user" # be careful with the exact name and prefix
    model = User
    def get_queryset(self):
        return User.objects.all()
    
def index(request):
    if request.user.is_authenticated:
        answer = "Logged user: " + request.user.username + "<br/>Page principale du logiciel de gestion de groupements d'achat en commun (GAC).<a href='http://127.0.0.1:8000/accounts/logout/'>Click here to log out.</a>"
    else:
        answer = "Page principale du logiciel de gestion de groupements d'achat en commun (GAC).<a href='http://127.0.0.1:8000/accounts/login/'>Click here to login.</a>" # horrible hack on many accounts
    return HttpResponse(answer)
