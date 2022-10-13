from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.TextField()
    company = models.TextField()
    color = models.TextField()
    RAM = models.TextField()
    memory = models.TextField()
    price = models.TextField()
    img_url = models.TextField()

    def __str__(self) -> str:
        return self.name