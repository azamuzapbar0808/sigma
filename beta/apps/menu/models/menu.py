from django.db import models

from apps.restaurant.models import Restaurant

from .category import Category


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='Заведение')
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Категория меню')

    def __str__(self):
        return self.name
