from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


def user_images(instance, filename):
    date_time = datetime.now().strftime("%Y_%m_%d,%H:%M:%S")
    saved_file_name = instance.user.username + "-" + date_time + ".jpg"
    return 'profile/{0}/{1}'.format(instance.user.username, saved_file_name)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    digital = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    manufacturer_country = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='items/')
    slug = models.SlugField(max_length=200, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    class Meta:
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to=user_images, default='profile/default/default.png')
    total_price = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return self.product.name

    def add_amount(self):
        amount = self.product.price * self.quantity
        profile = self.user.profile
        profile.total_price = profile.total_price + amount
        profile.save()
        return True
