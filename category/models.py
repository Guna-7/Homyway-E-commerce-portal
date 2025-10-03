from django.db import models

# Create your models here.
class Category(models.Model):
    Category_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100,unique=True)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='photos/category',blank=True)

    def __str__(self):
        return self.Category_name