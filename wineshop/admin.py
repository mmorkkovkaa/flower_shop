from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models

admin.site.register(models.Товары)
admin.site.register(models.Index)
admin.site.register(models.Сотрудники)
admin.site.register(models.ImageDev)
admin.site.register(models.Basket)
admin.site.register(models.ТоварВЗаказе)
admin.site.register(models.ОформленныйЗаказ)
admin.site.register(models.Отзыв)
admin.site.register(models.Поставщики)
admin.site.register(models.Клиенты)
admin.site.register(models.Review)


