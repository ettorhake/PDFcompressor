# 📋 Instructions pour publier sur GitHub

## 🚀 Étapes pour publier votre projet

### 1. Préparer les fichiers
```bash
# Se positionner dans le dossier du projet
cd "C:\Users\Jlauzes\Desktop\book"

# Copier le README principal pour GitHub
copy README_GITHUB.md README.md
```

### 2. Initialiser Git (si pas déjà fait)
```bash
# Initialiser le repository Git
git init

# Ajouter la remote vers votre repository GitHub
git remote add origin https://github.com/ettorhake/PDFcompressor.git
```

### 3. Préparer les fichiers pour le commit
```bash
# Ajouter tous les fichiers importants
git add README.md
git add pdf_compressor_gui.py
git add aggressive_compress.py
git add requirements.txt
git add LICENSE
git add CHANGELOG.md
git add CONTRIBUTING.md
git add .gitignore
git add build.py

# Vérifier les fichiers ajoutés
git status
```

### 4. Créer le premier commit
```bash
# Commit initial
git commit -m "🚀 Initial release - PDF Compressor v1.0

✨ Features:
- Interactive GUI with drag & drop support
- Adjustable compression parameters (JPEG quality, DPI)
- Real-time progress bar
- Portable Windows executable
- 70-90% file size reduction
- Visual quality preservation

🔧 Technical:
- Built with Python, tkinter, PyMuPDF, Pillow
- PyInstaller for executable creation
- Complete documentation and build scripts"
```

### 5. Pousser vers GitHub
```bash
# Pousser vers la branche main
git branch -M main
git push -u origin main
```

### 6. Créer une release (optionnel)
1. Aller sur https://github.com/ettorhake/PDFcompressor
2. Cliquer sur "Releases" puis "Create a new release"
3. Tag version: `v1.0.0`
4. Release title: `PDF Compressor v1.0.0 - Initial Release`
5. Description:
```markdown
## 🎉 Première version de PDF Compressor !

### ✨ Fonctionnalités principales
- Interface graphique intuitive avec glisser-déposer
- Compression PDF efficace (70-90% de réduction)
- Paramètres ajustables en temps réel
- Application portable Windows (aucune installation)
- Barre de progression et gestion d'erreurs

### 📥 Installation
1. Téléchargez `PDFCompressor-v1.0.0.zip`
2. Décompressez le fichier
3. Lancez `PDFCompressor.exe`

### 🔧 Paramètres recommandés
- **Usage général**: 150 DPI, 85% qualité
- **Compression maximale**: 100 DPI, 70% qualité
- **Qualité maximale**: 200 DPI, 90% qualité

### 📊 Performances
- PDF 30 MB → 6 MB (80% de réduction)
- PDF 50 MB → 8 MB (84% de réduction)
- PDF 100 MB → 15 MB (85% de réduction)
```

6. Attacher le fichier `PDFCompressor_Portable.zip` (à créer depuis le dossier)

## 🗂️ Fichiers à inclure dans le repository

### Fichiers principaux ✅
- [x] `README.md` (version GitHub)
- [x] `pdf_compressor_gui.py` (application principale)
- [x] `aggressive_compress.py` (moteur de compression)
- [x] `requirements.txt` (dépendances)
- [x] `LICENSE` (licence MIT)
- [x] `CHANGELOG.md` (historique des versions)
- [x] `CONTRIBUTING.md` (guide de contribution)
- [x] `.gitignore` (fichiers à ignorer)
- [x] `build.py` (script de build)

### Fichiers à exclure ❌
- `.venv/` (environnement virtuel)
- `build/`, `dist/` (fichiers de build temporaires)
- `*.pdf` (fichiers de test)
- `README_GITHUB.md` (renommé en README.md)

## 🎯 Prochaines étapes

1. **Publier** le code source
2. **Créer** une release avec l'exécutable
3. **Ajouter** des captures d'écran de l'interface
4. **Écrire** une meilleure description du projet
5. **Promouvoir** le projet sur les réseaux sociaux

## 📞 Commandes Git utiles

```bash
# Voir l'état des fichiers
git status

# Voir l'historique des commits
git log --oneline

# Pousser des changements
git add .
git commit -m "feat: description du changement"
git push

# Créer une branche
git checkout -b feature/nouvelle-fonctionnalite

# Fusionner une branche
git checkout main
git merge feature/nouvelle-fonctionnalite
```

## 🏷️ Tags recommandés pour le projet

- `pdf-compression`
- `python-gui`
- `tkinter`
- `pdf-tools`
- `file-compression`
- `windows-app`
- `portable-app`
- `drag-and-drop`