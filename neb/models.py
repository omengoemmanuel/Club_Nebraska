from django.db import models


# Create your models here.
# Menu category
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

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


# Special events
class Special(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    details = models.TextField()
    image = models.ImageField(upload_to='images/Specials', default='images/Specials/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Events
class Event(models.Model):
    event_type = models.CharField(max_length=100)
    event_price = models.DecimalField(max_digits=10, decimal_places=2)
    event_title = models.TextField(default='')
    features = models.TextField(help_text='Please insert each feature on a new line')
    event_description = models.TextField()
    image = models.ImageField(upload_to='images/Events', default='images/Events/default.jpg')

    def get_features_list(self):
        """splits features into list for easy template rendering"""
        return self.features.split("\n")

    def __str__(self):
        return self.event_type


# Book a table
class table(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    no_of_people = models.IntegerField()
    message = models.TextField()
    status = models.CharField(max_length=100, default='Pending')

    def __str__(self):
        return self.name


# Testimonials
class testimonials(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    testimony = models.TextField()
    image = models.ImageField(upload_to='images/Testimonials', default='images/Testimonials/default.jpg')

    def __str__(self):
        return self.name


# Gallery
class gallery(models.Model):
    image = models.ImageField(upload_to='images/Gallery', default='images/Gallery/default.jpg')

# Contact
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


# Staffs
class staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    X_link = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='images/Staff', default='images/Staff/default.jpg')

    def __str__(self):
        return self.name