
from django.contrib import admin
from django.urls import path
from app.views import heyView, ageView, orderView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hey/', heyView, name='hey'),
    path('age-in/', ageView, name='age'),
    path('order-total/', orderView, name='order')
    ]
 