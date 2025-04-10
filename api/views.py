from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Region, ProductCategory, Product, Market, MarketPrice,DashboardStat, MarketInsight,Ad
from .serializers import RegionSerializer, ProductCategorySerializer, ProductSerializer, MarketSerializer, MarketPriceSerializer,DashboardStatSerializer, MarketInsightSerializer,AdSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class MarketPriceViewSet(viewsets.ModelViewSet):
    queryset = MarketPrice.objects.all()
    serializer_class = MarketPriceSerializer

class DashboardStatViewSet(viewsets.ModelViewSet):
    queryset = DashboardStat.objects.all()
    serializer_class = DashboardStatSerializer

class MarketInsightViewSet(viewsets.ModelViewSet):
    queryset = MarketInsight.objects.all()
    serializer_class = MarketInsightSerializer

@api_view(['GET'])
def generate_market_comparison_data(request, product_id):
    market_prices = MarketPrice.objects.filter(product__id=product_id)
    serializer = MarketPriceSerializer(market_prices, many=True)
    return Response(serializer.data)
class MarketPriceViewSet(viewsets.ModelViewSet):
    queryset = MarketPrice.objects.all()
    serializer_class = MarketPriceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['product', 'market', 'region', 'date']
    search_fields = ['product__name', 'market__name', 'region__name']
    ordering_fields = ['date', 'price', 'change']

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filtres personnalisés
        products = self.request.query_params.get('products')
        if products:
            product_ids = products.split(',')
            queryset = queryset.filter(product__id__in=product_ids)

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset 
class AdListView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        return context