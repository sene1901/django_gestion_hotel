#!/usr/bin/env bash
# build.sh - Script de déploiement pour Render

# Exit immédiatement si une commande échoue
set -o errexit

echo " Début du build..."

# Installer les dépendances
echo " Installation des dépendances..."
pip install --upgrade pip
pip install -r requirements.txt

# Collecter les fichiers statiques
echo " Collecte des fichiers statiques..."
python manage.py collectstatic --no-input --clear

# Appliquer les migrations
echo " Application des migrations..."
python manage.py migrate --no-input

echo " Build terminé avec succès!"