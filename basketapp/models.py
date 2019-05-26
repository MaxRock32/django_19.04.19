from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='quantity', default=0)
    add_datetime = models.DateTimeField(verbose_name='datetime', auto_now_add=True)

    @property
    def get_product_total_price(self):
        return self.quantity * self.product.price

    @property
    def get_products_total_quantity_by_user(self):
        user_basket = Basket.objects.filter(user_id=self.user)
        # return sum([user_basket[i].quantity for i in range(len(user_basket))])
        return sum([item.quantity for item in user_basket])

    @property
    def get_products_total_price_by_user(self):
        user_basket = Basket.objects.filter(user_id=self.user)
        # return sum([user_basket[i].get_product_total_price for i in range(len(user_basket))])
        return sum([item.get_product_total_price for item in user_basket])
