# Contributing to PDF Compressor

Merci de votre intérêt pour contribuer à PDF Compressor ! Ce document fournit des lignes directrices pour contribuer au projet.

## 🚀 Comment contribuer

### 1. Reporter des bugs

Si vous trouvez un bug, veuillez créer une issue avec :
- **Titre descriptif** du problème
- **Description détaillée** du bug
- **Étapes pour reproduire** le problème
- **Version** de l'application utilisée
- **Système d'exploitation** et version
- **Captures d'écran** si applicable

### 2. Proposer des améliorations

Pour proposer une nouvelle fonctionnalité :
- Vérifiez d'abord si une issue similaire n'existe pas déjà
- Créez une issue avec le label "enhancement"
- Décrivez clairement la fonctionnalité souhaitée
- Expliquez pourquoi cette fonctionnalité serait utile

### 3. Contribuer au code

#### Prérequis
- Python 3.8+
- Git
- Connaissance de base de tkinter et PyMuPDF

#### Processus
1. **Fork** le repository
2. **Clonez** votre fork localement
```bash
git clone https://github.com/VOTRE_USERNAME/PDFcompressor.git
cd PDFcompressor
```

3. **Créez** une branche pour votre fonctionnalité
```bash
git checkout -b feature/ma-nouvelle-fonctionnalite
```

4. **Configurez** l'environnement de développement
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

5. **Implémentez** vos changements
6. **Testez** vos modifications
7. **Commitez** avec un message descriptif
```bash
git commit -m "feat: ajouter fonctionnalité de prévisualisation"
```

8. **Poussez** vers votre fork
```bash
git push origin feature/ma-nouvelle-fonctionnalite
```

9. **Créez** une Pull Request

## 📝 Standards de code

### Style Python
- Suivre PEP 8
- Utiliser des noms de variables et fonctions descriptifs en français
- Commenter le code complexe
- Docstrings pour les fonctions publiques

### Structure des commits
Utiliser le format conventional commits :
- `feat:` pour une nouvelle fonctionnalité
- `fix:` pour une correction de bug
- `docs:` pour la documentation
- `style:` pour les changements de style
- `refactor:` pour le refactoring
- `test:` pour les tests

### Tests
- Tester manuellement l'interface graphique
- Vérifier la compression sur différents types de PDF
- Tester sur différentes versions de Windows si possible

## 🏗️ Architecture du projet

```
PDFCompressor/
├── pdf_compressor_gui.py      # Interface graphique principale
├── aggressive_compress.py     # Moteur de compression
├── requirements.txt           # Dépendances
├── README.md                  # Documentation principale
└── docs/                      # Documentation additionnelle
```

### Composants principaux
- **Interface GUI** : tkinter avec drag & drop
- **Compression** : PyMuPDF + Pillow
- **Build** : PyInstaller pour l'exécutable

## 🐛 Debugging

### Logs
L'application affiche les erreurs dans l'interface. Pour le debugging avancé :
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Tests manuels
- Tester avec des PDF de différentes tailles
- Vérifier les paramètres de compression
- Tester le drag & drop
- Vérifier la barre de progression

## 📖 Documentation

Si vous modifiez des fonctionnalités :
- Mettez à jour le README si nécessaire
- Ajoutez des commentaires dans le code
- Mettez à jour le CHANGELOG.md

## ❓ Questions

Si vous avez des questions :
- Consultez les issues existantes
- Créez une nouvelle issue avec le label "question"
- Soyez précis dans votre question

## 🙏 Reconnaissance

Tous les contributeurs seront mentionnés dans le README. Merci pour votre aide !

---

En contribuant à ce projet, vous acceptez que vos contributions soient sous licence MIT.