from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "book" 


class Orders(models.Model):
    name = models.CharField(max_length=100)
    date = models.IntegerField()


    def __str__(self):
        return self.name

    class Meta:
        db_table = "orders"