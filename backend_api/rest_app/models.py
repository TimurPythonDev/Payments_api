from django.db import models
from django.contrib.auth.models import User




class Product(models.Model):
    name = models.CharField(max_length=220)
    price =  models.DecimalField(max_digits=9,decimal_places=2)
    product_image = models.ImageField(upload_to='product_img',)
    product_url = models.URLField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products"



class PaymentHistory(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)
    payment_status=models.BooleanField()


    def __str__(self):
        return self.product.name