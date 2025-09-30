# PDF Compressor

<div align="center">

![PDF Compressor Logo](https://img.shields.io/badge/PDF-Compressor-blue?style=for-the-badge&logo=adobe-acrobat-reader)

**Application complète pour comprimer facilement des fichiers PDF avec interface graphique**

[![Python Version](https://img.shields.io/badge/python-3.8+-blue?style=flat-square)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey?style=flat-square)](https://www.microsoft.com/windows)
[![Release](https://img.shields.io/badge/release-v1.0-green?style=flat-square)](https://github.com/ettorhake/PDFcompressor/releases)

[📥 Télécharger l'application](https://github.com/ettorhake/PDFcompressor/releases) • [📖 Documentation](#utilisation) • [🐛 Signaler un bug](https://github.com/ettorhake/PDFcompressor/issues)

</div>

## ✨ Fonctionnalités

- 🖱️ **Interface intuitive** avec glisser-déposer
- 📊 **Compression efficace** : réduction de 70-90% de la taille
- ⚙️ **Paramètres ajustables** : qualité JPEG et résolution DPI
- 📈 **Barre de progression** en temps réel
- 💾 **Totalement portable** : aucune installation requise
- 🛡️ **Sécurisé** : traitement local, aucun envoi en ligne
- 🎯 **Préserve la qualité visuelle** malgré la compression

## 📸 Aperçu

![Interface PDF Compressor](https://via.placeholder.com/600x400/f0f0f0/333333?text=Interface+PDF+Compressor)

## 🚀 Installation et Utilisation

### Option 1: Application Portable (Recommandée)

1. **Téléchargez** la dernière version depuis les [Releases](https://github.com/ettorhake/PDFcompressor/releases)
2. **Décompressez** le fichier zip
3. **Double-cliquez** sur `PDFCompressor.exe`
4. **Glissez votre PDF** dans la fenêtre ou cliquez pour sélectionner
5. **Ajustez les paramètres** si nécessaire
6. **Cliquez** sur "Comprimer le PDF"

### Option 2: Depuis le Code Source

```bash
# Cloner le repository
git clone https://github.com/ettorhake/PDFcompressor.git
cd PDFcompressor

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python pdf_compressor_gui.py
```

## ⚙️ Configuration

### Paramètres Recommandés

| Usage | DPI | Qualité JPEG | Résultat |
|-------|-----|--------------|----------|
| **Usage général** | 150 | 85% | Excellente qualité, bonne compression |
| **Fichiers très lourds** | 100 | 70% | Compression maximale |
| **Impression professionnelle** | 200 | 90% | Qualité maximale |

### Paramètres Avancés

- **Résolution DPI** : 100-300 (défaut: 150)
- **Qualité JPEG** : 30-95% (défaut: 85%)
- **Méthode** : Conversion PDF → Images → PDF compressé

## 📊 Performances

| Taille Originale | Taille Compressée | Réduction |
|------------------|-------------------|-----------|
| 30 MB | 6 MB | 80% |
| 50 MB | 8 MB | 84% |
| 100 MB | 15 MB | 85% |

## 🛠️ Développement

### Prérequis

- Python 3.8+
- pip

### Installation pour le développement

```bash
# Cloner le repository
git clone https://github.com/ettorhake/PDFcompressor.git
cd PDFcompressor

# Créer un environnement virtuel
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Installer les dépendances
pip install -r requirements.txt
```

### Structure du Projet

```
PDFCompressor/
├── 📄 pdf_compressor_gui.py      # Interface graphique principale
├── 📄 aggressive_compress.py     # Moteur de compression
├── 📄 requirements.txt           # Dépendances Python
├── 📄 LICENSE                    # Licence MIT
├── 📁 docs/                      # Documentation
└── 📁 releases/                  # Versions compilées
```

### Construire l'Exécutable

```bash
# Installer PyInstaller
pip install pyinstaller

# Créer l'exécutable
pyinstaller --onefile --windowed --name=PDFCompressor pdf_compressor_gui.py
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment procéder :

1. **Fork** le projet
2. **Créez** une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. **Commit** vos changements (`git commit -m 'Add some AmazingFeature'`)
4. **Push** vers la branche (`git push origin feature/AmazingFeature`)
5. **Ouvrez** une Pull Request

## 📋 Roadmap

- [ ] 🌍 Interface multilingue (anglais, français, espagnol)
- [ ] 🖼️ Prévisualisation avant/après compression
- [ ] 📱 Version web (Progressive Web App)
- [ ] 🔧 Compression par lots
- [ ] 📈 Graphiques de statistiques détaillées
- [ ] 🎨 Thèmes sombres/clairs

## ❓ FAQ

<details>
<summary><strong>Le texte reste-t-il sélectionnable après compression ?</strong></summary>

Non, le texte devient non-sélectionnable car il est converti en image. Cependant, la qualité visuelle reste excellente et le texte reste parfaitement lisible.

</details>

<details>
<summary><strong>L'application fonctionne-t-elle hors ligne ?</strong></summary>

Oui, l'application fonctionne entièrement en local. Aucune connexion internet n'est requise et aucun fichier n'est envoyé en ligne.

</details>

<details>
<summary><strong>Quels formats sont supportés ?</strong></summary>

Actuellement, seuls les fichiers PDF sont supportés en entrée et en sortie.

</details>

## 🐛 Problèmes Connus

- Sur certains systèmes Windows anciens, l'application peut nécessiter les Visual C++ Redistributables
- Les PDF avec des polices très spécifiques peuvent avoir un rendu légèrement différent

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciements

- [PyMuPDF](https://pymupdf.readthedocs.io/) pour le traitement des PDF
- [Pillow](https://python-pillow.org/) pour le traitement d'images
- [tkinterdnd2](https://pypi.org/project/tkinterdnd2/) pour le glisser-déposer

## 📞 Support

- 🐛 [Signaler un bug](https://github.com/ettorhake/PDFcompressor/issues)
- 💡 [Demander une fonctionnalité](https://github.com/ettorhake/PDFcompressor/issues)
- 📧 Contact: [Créer une issue](https://github.com/ettorhake/PDFcompressor/issues)

---

<div align="center">

**⭐ Si ce projet vous aide, n'hésitez pas à lui donner une étoile ! ⭐**

Fait avec ❤️ par [ettorhake](https://github.com/ettorhake)

</div>