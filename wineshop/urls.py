from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                    path('', views.index, name='index'),
                    path('tovary/', views.товары, name='товары'),
                    path('aboutus/', views.сотрудники, name='сотрудники'),
                    path('добавить_в_корзину/<int:товар_id>/', views.добавить_в_корзину, name='добавить_в_корзину'),
                    path('корзина/', views.корзина, name='корзина'),
                    path('оплатить_заказ/', views.оплатить_заказ, name='оплатить_заказ'),
                    path('все_заказы/', views.все_заказы, name='все_заказы'),
                     path('review/', views.review_page, name='review_page'),





              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
