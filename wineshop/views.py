from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import wineshop
from django.shortcuts import HttpResponseRedirect
from wineshop import models
from django.shortcuts import render, redirect, get_object_or_404
from .models import Basket, Товары , ОформленныйЗаказ, ТоварВЗаказе, Отзыв, Поставщики
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout



def index(request):
    index = models.Index.objects.all()
    поставщики = models.Поставщики.objects.all()
    return render(request, 'index.html', {'index': index, 'поставщики': поставщики})

def товары(request):
    товары = models.Товары.objects.all()
    отзывы = Отзыв.objects.all()
    return render(request, 'tovary.html', {'товары': товары, 'отзывы': отзывы})


def сотрудники(request):
    сотрудники = models.Сотрудники.objects.all()
    image = models.ImageDev.objects.all()
    клиенты = models.Клиенты.objects.all()

    context = {'сотрудники': сотрудники, 'image': image, 'клиенты': клиенты}

    return render(request, 'aboutus.html',context )




def добавить_в_корзину(request, товар_id):
    товар = Товары.objects.get(id=товар_id)
    активная_корзина, создана = Basket.objects.get_or_create(user=request.user, товар=товар)
    активная_корзина.quantity += 1
    активная_корзина.save()
    return redirect('товары')

def корзина(request):
    корзина = Basket.objects.filter(user=request.user)
    общая_стоимость = sum(item.товар.price  * item.quantity for item in корзина)
    return render(request, 'корзина.html', {'корзина': корзина, 'общая_стоимость': общая_стоимость})

@login_required
def оплатить_заказ(request):
    корзина = Basket.objects.filter(user=request.user)

    новый_заказ = ОформленныйЗаказ.objects.create(user=request.user, оплачен=True)

    for item in корзина:
        ТоварВЗаказе.objects.create(заказ=новый_заказ, товар=item.товар, количество=item.quantity)

    корзина.delete()

    return redirect('/')

def все_заказы(request):
    все_заказы = ОформленныйЗаказ.objects.all()
    return render(request, 'все_заказы.html', {'все_заказы': все_заказы})

def review_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_page')
    else:
        form = ReviewForm()
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'review_page.html', {'form': form, 'reviews': reviews})

def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    form = ReviewForm(instance=review)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_page')
    return render(request, 'edit_review.html', {'form': form})

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('review_page')
    return render(request, 'delete_review.html', {'review': review})

def product_details(request, product_id):
    product = get_object_or_404(Товары, pk=product_id)
    return render(request, 'product_details.html', {'product': product})