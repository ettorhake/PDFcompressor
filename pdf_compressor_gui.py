#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF Compressor GUI - Interface graphique pour compression PDF
Drag & Drop ou sélection de fichier pour compression automatique
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinterdnd2 as tkdnd
import fitz  # PyMuPDF
from PIL import Image
import os
import threading
from pathlib import Path
import time
import io

class PDFCompressorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Compressor - Glissez votre PDF ici")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.current_file = None
        self.is_processing = False
        
        self.setup_ui()
        self.setup_drag_drop()
    
    def setup_ui(self):
        """Créer l'interface utilisateur"""
        
        # Titre
        title_frame = tk.Frame(self.root, bg='#f0f0f0')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame, 
            text="🗜️ PDF Compressor", 
            font=('Arial', 24, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame, 
            text="Glissez un PDF ou cliquez pour sélectionner", 
            font=('Arial', 12),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        subtitle_label.pack()
        
        # Zone de drop
        self.drop_frame = tk.Frame(
            self.root, 
            bg='#ecf0f1', 
            relief='ridge', 
            bd=2,
            height=150
        )
        self.drop_frame.pack(pady=20, padx=30, fill='x')
        self.drop_frame.pack_propagate(False)
        
        self.drop_label = tk.Label(
            self.drop_frame,
            text="📁 Glissez votre PDF ici\nou cliquez pour sélectionner",
            font=('Arial', 14),
            bg='#ecf0f1',
            fg='#34495e',
            cursor='hand2'
        )
        self.drop_label.pack(expand=True)
        self.drop_label.bind('<Button-1>', self.select_file)
        
        # Paramètres de compression
        params_frame = tk.LabelFrame(
            self.root, 
            text="Paramètres de compression", 
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        params_frame.pack(pady=20, padx=30, fill='x')
        
        # Qualité JPEG
        quality_frame = tk.Frame(params_frame, bg='#f0f0f0')
        quality_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(
            quality_frame, 
            text="Qualité JPEG:", 
            font=('Arial', 10),
            bg='#f0f0f0'
        ).pack(side='left')
        
        self.quality_var = tk.IntVar(value=85)
        self.quality_scale = tk.Scale(
            quality_frame, 
            from_=30, 
            to=95, 
            orient='horizontal',
            variable=self.quality_var,
            bg='#f0f0f0'
        )
        self.quality_scale.pack(side='right', fill='x', expand=True, padx=(10, 0))
        
        # Résolution DPI
        dpi_frame = tk.Frame(params_frame, bg='#f0f0f0')
        dpi_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(
            dpi_frame, 
            text="Résolution DPI:", 
            font=('Arial', 10),
            bg='#f0f0f0'
        ).pack(side='left')
        
        self.dpi_var = tk.IntVar(value=150)
        dpi_values = [100, 150, 200, 300]
        self.dpi_combo = ttk.Combobox(
            dpi_frame, 
            textvariable=self.dpi_var,
            values=dpi_values,
            state='readonly',
            width=10
        )
        self.dpi_combo.pack(side='right')
        
        # Bouton de compression
        self.compress_btn = tk.Button(
            self.root,
            text="🗜️ Comprimer le PDF",
            font=('Arial', 14, 'bold'),
            bg='#3498db',
            fg='white',
            relief='flat',
            padx=30,
            pady=10,
            cursor='hand2',
            state='disabled',
            command=self.start_compression
        )
        self.compress_btn.pack(pady=20)
        
        # Barre de progression
        self.progress_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.progress_frame.pack(pady=10, padx=30, fill='x')
        
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            variable=self.progress_var,
            maximum=100
        )
        self.progress_bar.pack(fill='x', pady=5)
        
        self.status_label = tk.Label(
            self.progress_frame,
            text="Prêt à comprimer",
            font=('Arial', 10),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        self.status_label.pack()
        
        # Informations sur le fichier
        self.info_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.info_frame.pack(pady=10, padx=30, fill='x')
        
        self.file_info_label = tk.Label(
            self.info_frame,
            text="",
            font=('Arial', 10),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        self.file_info_label.pack()
    
    def setup_drag_drop(self):
        """Configurer le drag & drop"""
        self.drop_frame.drop_target_register(tkdnd.DND_FILES)
        self.drop_frame.dnd_bind('<<Drop>>', self.on_drop)
        
        # Effet visuel pour le drag over
        self.drop_frame.dnd_bind('<<DragEnter>>', self.on_drag_enter)
        self.drop_frame.dnd_bind('<<DragLeave>>', self.on_drag_leave)
    
    def on_drag_enter(self, event):
        """Effet visuel quand on survole avec un fichier"""
        self.drop_frame.configure(bg='#d5dbdb')
        self.drop_label.configure(bg='#d5dbdb')
    
    def on_drag_leave(self, event):
        """Retour à la normale"""
        self.drop_frame.configure(bg='#ecf0f1')
        self.drop_label.configure(bg='#ecf0f1')
    
    def on_drop(self, event):
        """Gestion du drop de fichier"""
        self.drop_frame.configure(bg='#ecf0f1')
        self.drop_label.configure(bg='#ecf0f1')
        
        files = self.root.tk.splitlist(event.data)
        if files:
            file_path = files[0]
            if file_path.lower().endswith('.pdf'):
                self.load_file(file_path)
            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner un fichier PDF (.pdf)")
    
    def select_file(self, event=None):
        """Sélection de fichier par dialogue"""
        file_path = filedialog.askopenfilename(
            title="Sélectionner un fichier PDF",
            filetypes=[("Fichiers PDF", "*.pdf"), ("Tous les fichiers", "*.*")]
        )
        if file_path:
            self.load_file(file_path)
    
    def load_file(self, file_path):
        """Charger un fichier PDF"""
        try:
            self.current_file = file_path
            
            # Obtenir les informations du fichier
            file_size = os.path.getsize(file_path) / (1024 * 1024)  # MB
            file_name = os.path.basename(file_path)
            
            # Obtenir le nombre de pages
            doc = fitz.open(file_path)
            page_count = len(doc)
            doc.close()
            
            # Mettre à jour l'interface
            self.drop_label.configure(
                text=f"✅ {file_name}\n{page_count} pages - {file_size:.1f} MB"
            )
            
            self.file_info_label.configure(
                text=f"Fichier chargé: {file_name} ({file_size:.1f} MB, {page_count} pages)"
            )
            
            self.compress_btn.configure(state='normal', bg='#27ae60')
            self.status_label.configure(text="Prêt à comprimer")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de charger le fichier:\n{str(e)}")
    
    def start_compression(self):
        """Démarrer la compression en arrière-plan"""
        if not self.current_file or self.is_processing:
            return
        
        self.is_processing = True
        self.compress_btn.configure(state='disabled', bg='#95a5a6')
        self.progress_var.set(0)
        self.status_label.configure(text="Compression en cours...")
        
        # Lancer la compression dans un thread séparé
        thread = threading.Thread(target=self.compress_pdf)
        thread.daemon = True
        thread.start()
    
    def compress_pdf(self):
        """Fonction de compression (adaptée du script original)"""
        try:
            input_path = self.current_file
            file_name = Path(input_path).stem
            output_path = str(Path(input_path).parent / f"{file_name}_compressed.pdf")
            
            # Paramètres
            dpi = self.dpi_var.get()
            jpeg_quality = self.quality_var.get()
            
            # Ouvrir le PDF
            doc = fitz.open(input_path)
            total_pages = len(doc)
            
            # Créer un nouveau PDF pour la sortie
            output_doc = fitz.open()
            
            for page_num in range(total_pages):
                # Mettre à jour la progression
                progress = (page_num / total_pages) * 100
                self.root.after(0, lambda p=progress: self.progress_var.set(p))
                self.root.after(0, lambda p=page_num+1, t=total_pages: 
                               self.status_label.configure(text=f"Traitement page {p}/{t}..."))
                
                # Charger la page
                page = doc[page_num]
                
                # Convertir en image
                mat = fitz.Matrix(dpi/72, dpi/72)
                pix = page.get_pixmap(matrix=mat)
                img_data = pix.tobytes("ppm")
                
                # Comprimer avec PIL
                img = Image.open(io.BytesIO(img_data))
                
                # Convertir en JPEG avec compression
                img_buffer = io.BytesIO()
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                img.save(img_buffer, format='JPEG', quality=jpeg_quality, optimize=True)
                img_buffer.seek(0)
                
                # Créer une nouvelle page et ajouter l'image
                page_rect = page.rect
                new_page = output_doc.new_page(width=page_rect.width, height=page_rect.height)
                
                # Insérer l'image compressée
                img_buffer.seek(0)
                new_page.insert_image(page_rect, stream=img_buffer.getvalue())
            
            # Sauvegarder
            output_doc.save(output_path, garbage=4, deflate=True)
            output_doc.close()
            doc.close()
            
            # Calculer les tailles
            original_size = os.path.getsize(input_path) / (1024 * 1024)
            compressed_size = os.path.getsize(output_path) / (1024 * 1024)
            reduction = ((original_size - compressed_size) / original_size) * 100
            
            # Finaliser l'interface
            self.root.after(0, lambda: self.progress_var.set(100))
            self.root.after(0, lambda: self.status_label.configure(
                text=f"✅ Terminé! {original_size:.1f}MB → {compressed_size:.1f}MB (-{reduction:.1f}%)"
            ))
            
            # Message de succès
            self.root.after(0, lambda: messagebox.showinfo(
                "Compression terminée",
                f"Fichier compressé avec succès!\n\n"
                f"Original: {original_size:.1f} MB\n"
                f"Compressé: {compressed_size:.1f} MB\n"
                f"Réduction: {reduction:.1f}%\n\n"
                f"Fichier sauvé: {os.path.basename(output_path)}"
            ))
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(
                "Erreur de compression",
                f"Une erreur s'est produite:\n{str(e)}"
            ))
        finally:
            self.is_processing = False
            self.root.after(0, lambda: self.compress_btn.configure(state='normal', bg='#27ae60'))

def main():
    """Fonction principale"""
    try:
        root = tkdnd.TkinterDnD.Tk()
        app = PDFCompressorGUI(root)
        root.mainloop()
    except ImportError:
        # Fallback sans drag & drop si tkinterdnd2 n'est pas disponible
        root = tk.Tk()
        app = PDFCompressorGUI(root)
        root.mainloop()

if __name__ == "__main__":
    main()