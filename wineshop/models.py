from django.db import models
from django.contrib.auth.models import User


class Index(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


# Create your models here.
class Товары(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')

    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    supplier_company = models.CharField(max_length=100)
    stock_quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    harvest_year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    variety = models.CharField(max_length=50)
    taste = models.CharField(max_length=50)
    classification = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Сотрудники(models.Model):
    имя = models.CharField(max_length=50)
    фамилия = models.CharField(max_length=50)
    стаж_работы = models.PositiveIntegerField()
    должность = models.CharField(max_length=100)
    телефон = models.CharField(max_length=15)
    почта = models.EmailField()
    место_жительства = models.CharField(max_length=100)
    любимое_вино = models.ForeignKey('Товары', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.фамилия}, {self.имя} - {self.должность}"

class ImageDev(models.Model):
    сотрудник = models.OneToOneField(Сотрудники, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='employee_images/')

    def __str__(self):
        return f"Изображение для {self.сотрудник.фамилия}, {self.сотрудник.имя}"


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    товар = models.ForeignKey(Товары, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.товар.title}'

class ТоварВЗаказе(models.Model):
    заказ = models.ForeignKey('ОформленныйЗаказ', related_name='товары_в_заказе', on_delete=models.CASCADE)
    товар = models.ForeignKey(Товары, on_delete=models.CASCADE)
    количество = models.IntegerField(default=0)

    def __str__(self):
        return f'Товар в заказе #{self.заказ.id} | {self.товар.title}'

class ОформленныйЗаказ(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    дата_заказа = models.DateTimeField(auto_now_add=True)
    оплачен = models.BooleanField(default=False)

    def __str__(self):
        return f'Заказ #{self.id} от {self.user.username}'

class Отзыв(models.Model):
    пользователь = models.ForeignKey(User, on_delete=models.CASCADE)
    товар = models.ForeignKey(Товары, on_delete=models.CASCADE, related_name='отзывы')
    имя = models.CharField(max_length=255)
    фамилия = models.CharField(max_length=255)
    текст = models.TextField()
    дата_отзыва = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отзыв от {self.пользователь.username} на товар {self.товар.title}'


class Поставщики(models.Model):
    company_name = models.CharField(max_length=100, verbose_name='Название компании')
    country = models.CharField(max_length=50, verbose_name='Страна')
    region = models.CharField(max_length=50, verbose_name='Регион')
    image = models.ImageField(upload_to='supplier_images/', verbose_name='Изображение')

    def __str__(self):
        return self.company_name

class Клиенты(models.Model):
    название_компании = models.CharField(max_length=255, blank=True, null=True)
    имя = models.CharField(max_length=100)
    фамилия = models.CharField(max_length=100)
    контакты = models.CharField(max_length=255, blank=True, null=True)
    картинка = models.ImageField(upload_to='client_images/', blank=True, null=True)
    отзыв = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.имя} {self.фамилия}"


class Review(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name