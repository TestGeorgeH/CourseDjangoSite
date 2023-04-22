from django.urls import path

from api_app.views import ProductAPIView

app_name = 'api_app'

urlpatterns = [
    path('product-list/', ProductAPIView.as_view(), name='product_list'),
    ]
