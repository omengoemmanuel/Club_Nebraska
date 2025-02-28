from django.db import models

# Create your models here.

class MenuCategory(models.Model):
    name= models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')
    image = models.ImageField(upload_to='images/Menu Items', default='images/Menu Items/default.jpg')

    def __str__(self):
        return self.name


class Special(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    details = models.TextField()
    image = models.ImageField(upload_to='images/Specials', default='images/Specials/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title