from django.contrib import admin
from django.urls import path, include
from project_sm.views import ProductsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', ProductsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
