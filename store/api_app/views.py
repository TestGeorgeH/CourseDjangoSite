from rest_framework.generics import ListAPIView

from products.models import Product
from products.serializers import ProductSerializers

class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
