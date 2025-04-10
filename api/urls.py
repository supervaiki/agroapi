from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegionViewSet, ProductCategoryViewSet, ProductViewSet, MarketViewSet, MarketPriceViewSet, DashboardStatViewSet, MarketInsightViewSet,generate_market_comparison_data,AdListView

router = DefaultRouter()
router.register(r'regions', RegionViewSet)
router.register(r'product-categories', ProductCategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'markets', MarketViewSet)
router.register(r'market-prices', MarketPriceViewSet)
router.register(r'dashboard-stats', DashboardStatViewSet)
router.register(r'market-insights', MarketInsightViewSet)


urlpatterns = [
    
    path('api/', include(router.urls)),
     path( 'api/generate-market-comparison-data/<str:product_id>/', generate_market_comparison_data, name='generate-market-comparison-data',),
      path('ads/', AdListView.as_view(), name='ad-list'),

]
