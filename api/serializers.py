from rest_framework import serializers
from .models import Region, ProductCategory, Product, Market, MarketPrice,HistoricalPrice,DashboardStat, MarketInsight,Ad
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']


class HistoricalPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPrice  # Ensure you have this model
        fields = ['date', 'price']
class DashboardStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardStat
        fields = ['title', 'value', 'change', 'change_label']

class MarketInsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketInsight
        fields = ['title', 'content']

class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    historical_prices = HistoricalPriceSerializer(many=True)  # Serialize historical prices

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'historical_prices']


class MarketSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = Market
        fields = ['id', 'name', 'region']


class MarketPriceSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    market = MarketSerializer()

    class Meta:
        model = MarketPrice
        fields = ['product', 'market', 'region', 'price', 'currency', 'unit', 'change', 'date'] 
class AdSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Ad
        fields = ['id', 'title', 'image', 'image_url', 'description']
    
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
