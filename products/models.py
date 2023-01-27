from django.db import models


class Product_Category(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return friendly_name


class Skin_Concern(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return friendly_name


class Product(models.Model):
    product_type = models.ForeignKey('Product_Category', null=True, blank=True,
                                     on_delete=models.SET_NULL)
    skin_type = models.ForeignKey('Skin_Concern', null=True, blank=True,
                                  on_delete=models.SET_NULL)
    line_number = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=1,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name