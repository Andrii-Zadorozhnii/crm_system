from django.shortcuts import render, redirect

from .forms import ClientForm
from .models import Clients, Deals, Tasks


# Create your views here.

def client_list(request):
    client = Clients.objects.all()
    return render(request,"crm/client_list.html", {'client':client})


def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'crm/add_client.html', {'form':form})