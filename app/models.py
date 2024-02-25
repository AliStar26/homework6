from django.db import models

class IceCreamKiosk(models.Model):
    city = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.city

class IceCream(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    city = models.ForeignKey(IceCreamKiosk, on_delete=models.CASCADE)
    
    def __str__(self):
     return self.name