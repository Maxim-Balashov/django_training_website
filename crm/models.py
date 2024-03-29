from django.db import models


class Orders(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя', blank=False)
    order_phone = models.CharField(max_length=200, verbose_name='Телефон', blank=False)

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'