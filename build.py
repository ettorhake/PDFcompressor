#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de build pour PDF Compressor
Crée l'exécutable portable Windows
"""

import subprocess
import sys
import shutil
import os
from pathlib import Path

def main():
    """Script principal de build"""
    print("🚀 PDF Compressor - Script de Build")
    print("=" * 50)
    
    # Vérifier que les fichiers existent
    required_files = ["pdf_compressor_gui.py", "requirements.txt"]
    for file in required_files:
        if not Path(file).exists():
            print(f"❌ Erreur: {file} non trouvé")
            return False
    
    # Nettoyer les anciens builds
    print("🧹 Nettoyage des anciens builds...")
    for folder in ["build", "dist", "__pycache__"]:
        if Path(folder).exists():
            shutil.rmtree(folder)
            print(f"   Supprimé: {folder}/")
    
    # Installer PyInstaller si nécessaire
    print("📦 Vérification de PyInstaller...")
    try:
        import PyInstaller
        print("   ✅ PyInstaller déjà installé")
    except ImportError:
        print("   📥 Installation de PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # Créer l'exécutable
    print("⚙️ Création de l'exécutable...")
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",                    # Un seul fichier
        "--windowed",                   # Interface graphique
        "--name=PDFCompressor",         # Nom de l'exécutable
        "--clean",                      # Nettoyer avant
        "--distpath=./dist",           # Dossier de sortie
        "pdf_compressor_gui.py"
    ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("   ✅ Compilation réussie!")
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Erreur de compilation:")
        print(f"   {e.stderr}")
        return False
    
    # Vérifier le fichier final
    exe_path = Path("dist/PDFCompressor.exe")
    if exe_path.exists():
        size_mb = exe_path.stat().st_size / (1024 * 1024)
        print(f"📦 Exécutable créé: {exe_path}")
        print(f"📏 Taille: {size_mb:.1f} MB")
    else:
        print("❌ Erreur: Exécutable non trouvé")
        return False
    
    # Créer le package de release
    print("📁 Création du package de release...")
    release_dir = Path("release")
    if release_dir.exists():
        shutil.rmtree(release_dir)
    release_dir.mkdir()
    
    # Copier les fichiers nécessaires
    files_to_copy = [
        ("dist/PDFCompressor.exe", "release/PDFCompressor.exe"),
        ("README_GITHUB.md", "release/README.txt"),
        ("LICENSE", "release/LICENSE.txt")
    ]
    
    for src, dst in files_to_copy:
        if Path(src).exists():
            shutil.copy2(src, dst)
            print(f"   ✅ Copié: {Path(dst).name}")
    
    # Créer un guide de démarrage rapide
    quick_guide = """PDF Compressor - Guide de Démarrage Rapide

UTILISATION:
1. Double-cliquez sur PDFCompressor.exe
2. Glissez votre fichier PDF dans la fenêtre
3. Ajustez les paramètres si nécessaire:
   - Qualité JPEG: 85% (recommandé)
   - Résolution DPI: 150 (recommandé)
4. Cliquez sur "Comprimer le PDF"
5. Récupérez votre fichier compressé

PARAMÈTRES:
- Usage général: 150 DPI, 85% qualité
- Compression max: 100 DPI, 70% qualité
- Qualité max: 200 DPI, 90% qualité

RÉSULTATS TYPIQUES:
- PDF 30 MB → 6 MB (80% de réduction)
- PDF 50 MB → 8 MB (84% de réduction)

Le fichier compressé sera créé dans le même dossier
avec le suffixe "_compressed".

© 2025 - PDF Compressor v1.0
"""
    
    with open("release/GUIDE_RAPIDE.txt", 'w', encoding='utf-8') as f:
        f.write(quick_guide)
    
    # Calculer la taille finale
    total_size = sum(f.stat().st_size for f in release_dir.rglob('*') if f.is_file())
    total_size_mb = total_size / (1024 * 1024)
    
    print(f"✅ Package de release créé: {release_dir.absolute()}")
    print(f"📏 Taille totale: {total_size_mb:.1f} MB")
    
    print("\n🎉 BUILD TERMINÉ AVEC SUCCÈS!")
    print("\n📦 Fichiers prêts pour distribution:")
    for file in sorted(release_dir.iterdir()):
        if file.is_file():
            size = file.stat().st_size / (1024 * 1024)
            print(f"   📄 {file.name} ({size:.1f} MB)")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)