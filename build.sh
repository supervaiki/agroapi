#!/bin/bash

set -e  # Arrête le script si une commande échoue


# Installer les dépendances
echo "Installation des dépendances..."
pip install -r requirements.txt

# Appliquer les migrations
echo "Application des migrations..."
python manage.py migrate

# Collecter les fichiers statiques
echo "Collecte des fichiers statiques..."
python manage.py collectstatic --no-input

# (Optionnel) Lancer le serveur
# echo "Démarrage du serveur..."
# python manage.py runserver

echo "✅ Build terminé avec succès !"
