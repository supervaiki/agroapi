from django.core.management.base import BaseCommand
from api.models import Region, ProductCategory, Product, Market, MarketPrice
from datetime import datetime
import random

class Command(BaseCommand):
    help = 'Insère des données fictives dans la base de données'

    def handle(self, *args, **kwargs):
        # Insertion des régions
        regions_data = [
            {'id': 'ndjamena', 'name': 'N\'Djamena'},
            {'id': 'logone', 'name': 'Logone'},
            {'id': 'mayo-kebbi', 'name': 'Mayo-Kebbi'},
            {'id': 'moyen-chari', 'name': 'Moyen-Chari'},
            {'id': 'ouaddai', 'name': 'Ouaddaï'},
            {'id': 'kanem', 'name': 'Kanem'},
            {'id': 'batha', 'name': 'Batha'},
            {'id': 'guera', 'name': 'Guéra'},
            {'id': 'salamat', 'name': 'Salamat'},
        ]
        for region in regions_data:
            Region.objects.create(id=region['id'], name=region['name'])

        # Insertion des catégories de produits
        product_categories = [
            'Céréales', 'Légumes', 'Fruits', 'Légumineuses', 'Produits animaux', 'Oléagineux'
        ]
        for category_name in product_categories:
            ProductCategory.objects.create(name=category_name)

        # Insertion des produits
        products_data = [
            {'id': 'mil', 'name': 'Mil', 'category': 'Céréales'},
            {'id': 'sorgho', 'name': 'Sorgho', 'category': 'Céréales'},
            {'id': 'mais', 'name': 'Maïs', 'category': 'Céréales'},
            {'id': 'riz', 'name': 'Riz', 'category': 'Céréales'},
            {'id': 'tomate', 'name': 'Tomate', 'category': 'Légumes'},
            {'id': 'oignon', 'name': 'Oignon', 'category': 'Légumes'},
            {'id': 'gombo', 'name': 'Gombo', 'category': 'Légumes'},
            {'id': 'ail', 'name': 'Ail', 'category': 'Légumes'},
            {'id': 'mangue', 'name': 'Mangue', 'category': 'Fruits'},
            {'id': 'banane', 'name': 'Banane', 'category': 'Fruits'},
            {'id': 'goyave', 'name': 'Goyave', 'category': 'Fruits'},
            {'id': 'niebe', 'name': 'Niébé', 'category': 'Légumineuses'},
            {'id': 'arachide', 'name': 'Arachide', 'category': 'Oléagineux'},
            {'id': 'sesame', 'name': 'Sésame', 'category': 'Oléagineux'},
            {'id': 'viande-boeuf', 'name': 'Viande de bœuf', 'category': 'Produits animaux'},
            {'id': 'poulet', 'name': 'Poulet', 'category': 'Produits animaux'},
            {'id': 'lait', 'name': 'Lait', 'category': 'Produits animaux'}
        ]
        for product in products_data:
            category = ProductCategory.objects.get(name=product['category'])
            Product.objects.create(id=product['id'], name=product['name'], category=category)

        # Insertion des marchés
        markets_data = [
            {'id': 'marche-central', 'name': 'Marché Central', 'region': 'ndjamena'},
            {'id': 'marche-dembé', 'name': 'Marché de Dembé', 'region': 'ndjamena'},
            {'id': 'marche-moundou', 'name': 'Marché de Moundou', 'region': 'logone'},
            {'id': 'marche-sarh', 'name': 'Marché de Sarh', 'region': 'moyen-chari'},
            {'id': 'marche-abeche', 'name': 'Marché d\'Abéché', 'region': 'ouaddai'},
            {'id': 'marche-bongor', 'name': 'Marché de Bongor', 'region': 'mayo-kebbi'},
            {'id': 'marche-bol', 'name': 'Marché de Bol', 'region': 'kanem'},
            {'id': 'marche-mongo', 'name': 'Marché de Mongo', 'region': 'guera'}
        ]
        for market in markets_data:
            region = Region.objects.get(id=market['region'])
            Market.objects.create(id=market['id'], name=market['name'], region=region)

        # Insertion des prix (Données générées aléatoirement)
        products = Product.objects.all()
        markets = Market.objects.all()
        for i in range(100):  # Générer 100 prix aléatoires
            product = random.choice(products)
            market = random.choice(markets)
            base_price = random.randint(20000, 60000)  # Prix de base aléatoire
            change = random.uniform(-15, 15)
            price_date = datetime.today().strftime('%Y-%m-%d')
            MarketPrice.objects.create(
                product=product,
                market=market,
                price=base_price,
                currency='XAF',
                unit='Par sac',
                change=change,
                date=price_date
            )

        self.stdout.write(self.style.SUCCESS('Données insérées avec succès!'))
