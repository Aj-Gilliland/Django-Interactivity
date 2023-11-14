
from django.contrib import admin
from django.urls import path
from app.views import aView,bView,cView,dView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warmup-2/font-times/', aView),
    path('logic-2/no-teen-sum/', bView),
    path('string-2/xyz-there/', cView),
    path('list-2/centered-average/', dView)
    ]
