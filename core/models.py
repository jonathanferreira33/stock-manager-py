from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    amount = models.IntegerField()

    def __str__(self):
        return self.product_name
    

class InventoryMovement(models.Model):
    release_date = models.DateField()
    user = models.CharField(max_length=50)

    def __str__(self):
        return self.release_date
        
