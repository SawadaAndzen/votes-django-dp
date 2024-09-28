from django.db import models


class Product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    price = models.DecimalField(max_digits = 2, decimal_places = 1)
    
    def __str__(self):
        return f"{self.name} - {self.price}$"
    
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete = models.DO_NOTHING, related_name = "reviews")
    author = models.CharField(max_length = 50)
    text = models.TextField()
    rating = models.IntegerField()
    
    def __str__(self):
        return f"{self.author}: {self.product} - {self.rating}"