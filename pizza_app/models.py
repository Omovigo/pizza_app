from django.db import models

class pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='pizzas/')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class pizzatoppings(models.Model):
    pizza = models.ForeignKey(pizza, on_delete=models.CASCADE)
    topping = models.ForeignKey(topping, on_delete=models.CASCADE)
