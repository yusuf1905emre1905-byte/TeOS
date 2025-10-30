import tkinter as tk
from tkinter import filedialog, messagebox
import json, os

class TPKCreator(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("TPK Creator")
        self.geometry("400x400")
        self.config(bg="#222")
        tk.Label(self, text="Uygulama Adı:", fg="white", bg="#222").pack()
        self.name_entry = tk.Entry(self); self.name_entry.pack()

        tk.Label(self, text="Açıklama:", fg="white", bg="#222").pack()
        self.desc_entry = tk.Entry(self); self.desc_entry.pack()

        tk.Button(self, text="TPK Oluştur", command=self.save_tpk).pack(pady=20)

    def save_tpk(self):
        name = self.name_entry.get()
        desc = self.desc_entry.get()
        if not name:
            messagebox.showerror("Hata", "İsim gerekli!")
            return
        tpk = {"name": name, "description": desc}
        path = filedialog.asksaveasfilename(defaultextension=".tpk", filetypes=[("TeOS Paketleri","*.tpk")])
        if path:
            json.dump(tpk, open(path,"w"))
            messagebox.showinfo("Başarılı", f"{name} adlı TPK oluşturuldu!")
          
