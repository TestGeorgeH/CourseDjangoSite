from django.db import models

from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class BasketQuerySet(models.QuerySet):
    def total_quantity(self):
        return sum(basket.quantity for basket in self)

    def total_sum(self):
        return sum(basket.sum() for basket in self)  # self == all baskets


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f"{self.user} | {self.product}, {self.quantity}"

    def sum(self):
        return self.product.price * self.quantity
