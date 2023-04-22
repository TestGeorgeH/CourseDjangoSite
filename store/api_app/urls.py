from django.urls import path, include

from rest_framework import routers

from api_app.views import ProductModelViewSet

app_name = 'api_app'

router = routers.DefaultRouter()
router.register(r'products', ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]
