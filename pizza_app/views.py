from django.shortcuts import render
from .models import pizza
from .models import sides
from .models import drink

# Create your views here.
def index(request):
    return render(request, 'pizza_app/index.html')

def pizza_page(request):
    pizza_page = pizza.objects.all()
    context = {'pizza_page': pizza_page}
    return render(request, 'pizza_app/pizza_page.html', context)

def side_page(request):
    side_page = sides.objects.all()
    context = {'side_page': side_page}
    return render(request, 'pizza_app/side_page.html', context)

def drink_page(request):
    drink_page = drink.objects.all()
    context= {'drink_page': drink_page}
    return render(request, 'pizza_app/drink_page.html', context)