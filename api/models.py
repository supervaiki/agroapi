from django.db import models
from django.utils import timezone
# Model for Region
class Region(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model for ProductCategory
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model for Product
class Product(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Model for Market
class Market(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Model for MarketPrice
class MarketPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    region = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    unit = models.CharField(max_length=10)
    change = models.IntegerField()  # Percentage change
    date = models.DateField()

    def __str__(self):
        return f"{self.product.name} - {self.market.name} - {self.date}"
        
class HistoricalPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='historical_prices')  # Relation avec Product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Le prix à un moment donné
    date = models.DateField(default=timezone.now)  # La date à laquelle ce prix a été enregistré
    
    class Meta:
        ordering = ['date']  # Trier par date, du plus ancien au plus récent

    def __str__(self):
        return f"{self.product.name} - {self.price} XAF le {self.date}"
        
class DashboardStat(models.Model):
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    change = models.FloatField()
    change_label = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class MarketInsight(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title 

class Ad(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ads/')
    description = models.TextField()

    def __str__(self):
        return self.title