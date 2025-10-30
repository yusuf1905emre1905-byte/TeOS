import tkinter as tk
from tkinter import messagebox
import random

class UserTV(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("User TV / TeShort")
        self.geometry("600x400")
        self.config(bg="#111")
        tk.Label(self, text="📺 UserTV - Kısa Videolar", fg="white", bg="#111", font=("Arial",16)).pack(pady=10)
        self.videos = [
            "🐱 Süper Cat: Bissy Film",
            "🐕 Funny Dog Dance",
            "🐦 Kuşun Mükemmel Şarkısı",
            "🐍 Takky vs Yılan Mini Movie"
        ]
        tk.Button(self, text="🎬 Rastgele Video Aç", command=self.play_random).pack(pady=20)

    def play_random(self):
        v = random.choice(self.videos)
        messagebox.showinfo("Oynatılıyor", f"{v}\n(Ekranda video simülasyonu)")
      
