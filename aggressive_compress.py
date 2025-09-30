#!/usr/bin/env python3
"""
Compression PDF agressive avec conversion en images puis reconversion
Cette méthode garantit une compression maximale mais peut affecter la qualité
"""

import fitz  # PyMuPDF
import os
from PIL import Image
import io

def pdf_to_images_to_pdf(input_path, output_path, dpi=150, quality=85):
    """
    Convertit le PDF en images puis recrée un PDF compressé
    Cette méthode garantit une compression importante
    
    Args:
        input_path (str): PDF d'origine
        output_path (str): PDF de sortie
        dpi (int): Résolution pour la conversion
        quality (int): Qualité JPEG
    """
    print(f"🔄 Conversion PDF → Images → PDF")
    print(f"📊 DPI : {dpi}")
    print(f"🖼️  Qualité : {quality}%")
    print("=" * 50)
    
    # Ouvrir le PDF original
    doc = fitz.open(input_path)
    
    # Créer un nouveau PDF
    new_doc = fitz.open()
    
    total_pages = len(doc)
    print(f"📄 Pages à traiter : {total_pages}")
    
    for page_num in range(total_pages):
        print(f"🔄 Page {page_num + 1}/{total_pages}...")
        
        page = doc[page_num]
        
        # Convertir la page en image avec la résolution spécifiée
        mat = fitz.Matrix(dpi/72, dpi/72)  # 72 DPI est la base
        pix = page.get_pixmap(matrix=mat)
        
        # Convertir en bytes
        img_data = pix.tobytes("jpeg", jpg_quality=95)  # Qualité élevée pour la conversion initiale
        
        # Ouvrir avec Pillow pour compression finale
        image = Image.open(io.BytesIO(img_data))
        
        print(f"  📐 Taille image : {image.size[0]}x{image.size[1]}")
        
        # Appliquer la compression finale
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG", quality=quality, optimize=True)
        final_img_data = buffer.getvalue()
        
        # Calculer la réduction
        original_size = len(img_data)
        final_size = len(final_img_data)
        reduction = (1 - final_size / original_size) * 100
        print(f"  💾 Compression : {original_size/1024:.1f}KB → {final_size/1024:.1f}KB (-{reduction:.1f}%)")
        
        # Créer une nouvelle page dans le nouveau document
        page_width = image.size[0] * 72 / dpi  # Convertir en points PDF
        page_height = image.size[1] * 72 / dpi
        
        new_page = new_doc.new_page(width=page_width, height=page_height)
        
        # Insérer l'image compressée
        rect = fitz.Rect(0, 0, page_width, page_height)
        new_page.insert_image(rect, stream=final_img_data)
    
    # Sauvegarder le nouveau PDF
    print(f"\n💾 Sauvegarde du PDF final...")
    new_doc.save(output_path, garbage=4, deflate=True, clean=True)
    new_doc.close()
    doc.close()
    
    return os.path.getsize(output_path)

def progressive_aggressive_compression(input_path, target_mb=9.5):
    """
    Compression progressive avec différents réglages DPI/qualité
    """
    print("🎯 Compression progressive agressive...")
    
    # Paramètres : (dpi, qualité)
    settings = [
        (200, 90),  # Très haute qualité
        (150, 85),  # Haute qualité
        (150, 75),  # Bonne qualité
        (120, 70),  # Qualité moyenne
        (100, 65),  # Qualité réduite
        (80, 60),   # Basse qualité
        (72, 55),   # Très basse qualité
    ]
    
    for dpi, quality in settings:
        output_path = f"jlauzesbook_dpi{dpi}_q{quality}.pdf"
        
        print(f"\n🔄 Essai DPI {dpi}, qualité {quality}%...")
        
        try:
            final_size = pdf_to_images_to_pdf(input_path, output_path, dpi, quality)
            final_mb = final_size / 1024 / 1024
            
            original_size = os.path.getsize(input_path)
            reduction = (1 - final_size / original_size) * 100
            
            print(f"📊 Résultat : {final_mb:.2f} MB (réduction {reduction:.1f}%)")
            
            if final_mb <= target_mb:
                print(f"🎉 OBJECTIF ATTEINT ! ({final_mb:.2f} MB <= {target_mb} MB)")
                
                # Nettoyer les autres fichiers
                for d, q in settings:
                    temp_file = f"jlauzesbook_dpi{d}_q{q}.pdf"
                    if temp_file != output_path and os.path.exists(temp_file):
                        os.remove(temp_file)
                
                return output_path, final_mb
            else:
                print(f"⚠️  Encore trop gros : {final_mb:.2f} MB")
                # Supprimer ce fichier pour économiser l'espace
                os.remove(output_path)
                
        except Exception as e:
            print(f"❌ Erreur DPI {dpi}, qualité {quality}% : {e}")
            if os.path.exists(output_path):
                os.remove(output_path)
            continue
    
    return None, None

if __name__ == "__main__":
    input_file = "jlauzesbook.pdf"
    
    if not os.path.exists(input_file):
        print(f"❌ Fichier non trouvé : {input_file}")
        exit(1)
    
    print("🚀 COMPRESSION AGRESSIVE PDF")
    print("⚠️  Conversion en images pour compression maximale")
    print("📝 Note: Le texte deviendra non-sélectionnable")
    print("🎯 Objectif : < 10 MB")
    print("=" * 60)
    
    final_file, final_mb = progressive_aggressive_compression(input_file, 9.5)
    
    if final_file and final_mb:
        # Renommer le fichier final
        final_name = "jlauzesbook_compressed_aggressive.pdf"
        if os.path.exists(final_name):
            os.remove(final_name)
        os.rename(final_file, final_name)
        
        print(f"\n🏆 COMPRESSION AGRESSIVE RÉUSSIE !")
        print(f"📁 Fichier final : {final_name}")
        print(f"📊 Taille finale : {final_mb:.2f} MB")
        print(f"⚠️  Le texte est maintenant sous forme d'image")
        print(f"📧 Prêt pour envoi !")
        
        # Afficher les statistiques
        original_size = os.path.getsize(input_file)
        total_reduction = (1 - (final_mb * 1024 * 1024) / original_size) * 100
        print(f"📉 Réduction totale : {total_reduction:.1f}%")
        
    else:
        print(f"\n⚠️  Même avec compression maximale, impossible d'atteindre 10 MB.")
        print(f"💡 Le contenu du PDF est très dense en images haute résolution.")
        
        # Proposer une solution alternative
        print(f"\n🔧 SOLUTIONS ALTERNATIVES :")
        print(f"1. Diviser le PDF en plusieurs parties")
        print(f"2. Utiliser un outil externe comme Adobe Acrobat")
        print(f"3. Réduire davantage la résolution (< 72 DPI)")
        
        # Créer quand même un fichier très compressé pour test
        print(f"\n🔄 Création d'un fichier ultra-compressé pour test...")
        try:
            test_file = "jlauzesbook_ultra_compressed.pdf"
            size = pdf_to_images_to_pdf(input_file, test_file, 50, 40)  # Très basse qualité
            test_mb = size / 1024 / 1024
            print(f"📁 Fichier test : {test_file}")
            print(f"📊 Taille : {test_mb:.2f} MB")
        except:
            print(f"❌ Impossible de créer le fichier test")