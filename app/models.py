from tabnanny import verbose
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="Nom de la categorie",max_length=50)
    desc = models.TextField("Description")
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    desc = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

