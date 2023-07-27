from django.contrib import admin

from .models import pizza, topping, pizzatoppings, sides, drink
admin.site.register(pizza)
admin.site.register(topping)
admin.site.register(pizzatoppings)
admin.site.register(sides)
admin.site.register(drink)