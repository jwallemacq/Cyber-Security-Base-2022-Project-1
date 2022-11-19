from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Product

class ProductsByUserListView(LoginRequiredMixin,generic.ListView):
    model = Product
#    template_name = 'gac/product_list_user.html'
    def get_queryset(self):
        return Product.objects.filter(supplier=self.request.user)

def index(request):
    return HttpResponse("Page principale du logiciel de gestion de groupements d'achat en commun (GAC).<a href='http://127.0.0.1:8000/accounts/login/'>Click here to login.</a><a href='http://127.0.0.1:8000/accounts/logout/'>Click here to log out.</a>") # horrible hack on many accounts
