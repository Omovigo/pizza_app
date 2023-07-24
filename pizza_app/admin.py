from django.contrib import admin

from .models import pizza, topping, pizzatoppings
admin.site.register(pizza)
admin.site.register(topping)
admin.site.register(pizzatoppings)
