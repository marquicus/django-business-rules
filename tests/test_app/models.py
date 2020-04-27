from django.db import models


class Product(models.Model):
    name = models.TextField()
    related_products = models.ManyToManyField('Product', blank=True)
    current_inventory = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    @property
    def orders(self):
        return list(self.productorder_set.all())

    def __str__(self):
        return '{}'.format(self.name)


class ProductOrder(models.Model):
    expiration_date = models.DateField()
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.product, self.quantity, self.expiration_date)
