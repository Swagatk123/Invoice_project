from django.db import models

# Create your models here.
class Invoice(models.Model):
    date = models.DateField()
    customer_name = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name
    

class Invoice_detail(models.Model):
    Invoice = models.ForeignKey(Invoice,related_name ='details',on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description
    