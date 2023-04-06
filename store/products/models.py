import stripe

from django.db import models
from django.conf import settings

from users.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY

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
    stripe_products_price_id = models.CharField(max_length=128, blank=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.stripe_products_price_id:
            stripe_products_price_id = self.create_stripe_product_price()
            self.stripe_products_price_id = stripe_products_price_id['id']

        super(Product, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def create_stripe_product_price(self):
        stripe_product = stripe.Product.create(name=self.name)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'],
            unit_amount=round(self.price*100),
            currency='rub'
        )

        return stripe_product_price



class BasketQuerySet(models.QuerySet):
    def total_quantity(self):
        return sum(basket.quantity for basket in self)

    def total_sum(self):
        return sum(basket.sum() for basket in self)  # self == all baskets

    def stripe_products(self):
        line_items = []
        for basket in self:
            item = {
                'price': basket.product.stripe_products_price_id,
                'quantity': basket.quantity,
            }
            line_items.append(item)
        return line_items

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
