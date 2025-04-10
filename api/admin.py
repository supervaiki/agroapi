from django.contrib import admin
from .models import Region, ProductCategory, Product, Market, MarketPrice,HistoricalPrice,DashboardStat,MarketInsight,Ad

# Enregistrer les modèles dans l'admin
admin.site.register(Region)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Market)
admin.site.register(MarketPrice)
admin.site.register(DashboardStat)
admin.site.register(MarketInsight)

# Enregistrer le modèle Ad
admin.site.register(Ad)

@admin.register(HistoricalPrice)
class HistoricalPriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'date')
    list_filter = ('date', 'product')
    search_fields = ('product__name',)
