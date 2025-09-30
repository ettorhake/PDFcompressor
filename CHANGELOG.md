# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-09-30

### Ajouté
- Interface graphique complète avec glisser-déposer
- Support de la compression PDF avec paramètres ajustables
- Barre de progression en temps réel
- Application portable Windows (.exe)
- Paramètres de qualité JPEG (30-95%)  
- Paramètres de résolution DPI (100-300)
- Gestion d'erreurs complète
- Documentation utilisateur complète
- Scripts de build automatisés

### Fonctionnalités
- Compression PDF de 70-90% en moyenne
- Interface drag & drop intuitive
- Préservation de la qualité visuelle
- Traitement local sécurisé (pas d'envoi en ligne)
- Compatible Windows 10/11
- Aucune installation requise pour la version portable

### Technique
- Basé sur PyMuPDF pour le traitement PDF
- Utilise Pillow pour la compression d'images
- Interface tkinter avec tkinterdnd2
- Build PyInstaller pour l'exécutable
- Architecture modulaire Python