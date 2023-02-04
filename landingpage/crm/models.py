from django.db import models


# Create your models here.
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)  # Автосоздание даты создания поля
    order_name = models.CharField(max_length=200, verbose_name="Имя")  # Поле для имени с длиной 200
    order_phone = models.CharField(max_length=200, verbose_name="Телефон")  # Поле для телефона с длиной 200

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
