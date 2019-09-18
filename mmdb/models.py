from django.db import models

# Create your models here.
class customer(models.Model):
    fname = models.CharField(max_length=254)
    lname = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=254)

    class Meta:
        db_table = 'customer'