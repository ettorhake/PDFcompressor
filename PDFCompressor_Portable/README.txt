# PDF Compressor - Application Portable

## 📋 Description
Application portable pour comprimer facilement vos fichiers PDF.
Réduction de taille de 70-90% tout en préservant la qualité visuelle.

## 🚀 Comment utiliser

### Étape 1: Lancer l'application
- Double-cliquez sur `PDFCompressor.exe`
- L'interface graphique s'ouvre

### Étape 2: Sélectionner votre PDF
- **Méthode 1**: Glissez-déposez votre fichier PDF dans la zone grise
- **Méthode 2**: Cliquez dans la zone grise pour ouvrir le sélecteur de fichier

### Étape 3: Ajuster les paramètres (optionnel)
- **Qualité JPEG**: Curseur de 30% à 95%
  - 85% = Recommandé (bon équilibre taille/qualité)
  - 95% = Qualité maximale (fichier plus lourd)
  - 70% = Compression maximum (fichier plus léger)
  
- **Résolution DPI**: Menu déroulant
  - 150 DPI = Recommandé (bonne qualité d'impression)
  - 200 DPI = Haute qualité
  - 100 DPI = Compression maximum

### Étape 4: Comprimer
- Cliquez sur "🗜️ Comprimer le PDF"
- La barre de progression montre l'avancement
- Le fichier compressé est sauvé automatiquement avec le suffixe "_compressed"

## 📊 Résultats typiques
- **PDF de 30 MB** → **6 MB** (80% de réduction)
- **PDF de 50 MB** → **8 MB** (84% de réduction)
- **PDF de 100 MB** → **15 MB** (85% de réduction)

## ⚙️ Paramètres recommandés selon l'usage

### Usage général (documents, livres)
- **DPI**: 150
- **Qualité**: 85%
- **Résultat**: Excellente qualité, bonne compression

### Fichiers très lourds (>50 MB)
- **DPI**: 100
- **Qualité**: 70%
- **Résultat**: Compression maximale, qualité correcte

### Impression professionnelle
- **DPI**: 200
- **Qualité**: 90%
- **Résultat**: Qualité maximale, compression modérée

## ⚠️ Important à savoir
- Le texte devient non-sélectionnable (converti en image)
- La qualité visuelle est préservée
- Tous les contenus (textes, images, graphiques) sont conservés
- Le fichier original n'est jamais modifié

## 🔧 Informations techniques
- **Compatibilité**: Windows 10/11
- **Installation**: Aucune installation requise
- **Portable**: Peut être exécuté depuis n'importe quel dossier
- **Taille**: ~90 MB (application complète et autonome)
- **Dépendances**: Aucune (tout est inclus)

## 🆘 Résolution de problèmes

### L'application ne se lance pas
- Vérifiez que vous êtes sur Windows 10 ou 11
- Essayez de lancer en tant qu'administrateur (clic droit → "Exécuter en tant qu'administrateur")

### Erreur lors de la compression
- Vérifiez que le fichier PDF n'est pas ouvert dans un autre programme
- Assurez-vous d'avoir suffisamment d'espace disque libre
- Essayez avec des paramètres moins élevés (DPI plus bas, qualité plus basse)

### Le fichier compressé est trop lourd
- Réduisez la qualité JPEG (70-80%)
- Diminuez la résolution DPI (100-120)

### La qualité n'est pas suffisante
- Augmentez la qualité JPEG (90-95%)
- Augmentez la résolution DPI (200-300)

## 📞 Support
Cette application est basée sur des technologies open-source:
- Python + tkinter (interface)
- PyMuPDF (traitement PDF)
- Pillow (traitement d'images)

---

© 2025 - PDF Compressor v1.0
Application portable et gratuite
