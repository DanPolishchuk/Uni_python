from django.contrib import admin
from django.urls import path, include
from sneakers_hub_shop import views

urlpatterns = [
    path("", include("sneakers_hub_shop.urls")),
    path('admin/', admin.site.urls),
]
