# gui/window_manager.py

import tkinter as tk

class AppWindow(tk.Toplevel):
    def __init__(self, master, title="Uygulama", on_close=None):
        super().__init__(master)
        self.title(title)
        self.geometry("800x600")

        # Üst menü çubuğu
        title_bar = tk.Frame(self, bg="#222", height=30)
        title_bar.pack(fill=tk.X, side=tk.TOP)

        # Başlık
        title_label = tk.Label(title_bar, text=title, bg="#222", fg="white")
        title_label.pack(side=tk.LEFT, padx=10)

        # Kapat düğmesi
        close_btn = tk.Button(title_bar, text="✖", bg="#900", fg="white", command=self.close_app)
        close_btn.pack(side=tk.RIGHT, padx=5)

        # Ana içerik
        self.content = tk.Frame(self, bg="#111")
        self.content.pack(fill=tk.BOTH, expand=True)

        self.on_close = on_close

    def close_app(self):
        if self.on_close:
            self.on_close()
        self.destroy()
# gui/desktop.py
import tkinter as tk
from gui.window_manager import AppWindow

class TeOSDesktop(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Free TeOS Desktop")
        self.geometry("1024x640")
        self.config(bg="#0d0d0d")

        # Arka plan
        bg = tk.Label(self, bg="#0d0d0d")
        bg.pack(fill=tk.BOTH, expand=True)

        # Görev çubuğu
        self.taskbar = tk.Frame(self, bg="#222", height=40)
        self.taskbar.pack(fill=tk.X, side=tk.BOTTOM)

        # Başlat tuşu
        start_btn = tk.Button(self.taskbar, text="🔨 TeOS", bg="#444", fg="white",
                              command=self.toggle_menu)
        start_btn.pack(side=tk.LEFT, padx=5)

        # Başlat menüsü (başta gizli)
        self.menu_frame = tk.Frame(self, bg="#222", width=250, height=400)
        self.menu_frame.place(x=0, y=240)
        self.menu_frame.pack_propagate(False)
        self.menu_frame.lower()  # gizle

        # Menü içeriği (uygulamalar)
        apps = [
            ("📁  TeFiles", self.open_tefiles),
            ("🛍️  TeStore", self.open_testore),
            ("🤖  TekonAI", self.open_tekonai),
            ("🎮  TePlay", self.open_teplay),
            ("🎬  UserTV", self.open_usertv),
            ("⚙️  Ayarlar", self.open_settings),
        ]
        for name, cmd in apps:
            tk.Button(self.menu_frame, text=name, bg="#333", fg="white", anchor="w",
                      command=cmd).pack(fill=tk.X, pady=2, padx=5)

        # Durum
        self.menu_visible = False

    def toggle_menu(self):
        self.menu_visible = not self.menu_visible
        if self.menu_visible:
            self.menu_frame.lift()
        else:
            self.menu_frame.lower()

    # --- Uygulamalar ---
    def open_tefiles(self): AppWindow(self, "TeFiles")
    def open_testore(self): AppWindow(self, "TeStore")
    def open_tekonai(self): AppWindow(self, "TekonAI")
    def open_teplay(self): AppWindow(self, "TePlay")
    def open_usertv(self): AppWindow(self, "UserTV")
    def open_settings(self): AppWindow(self, "Ayarlar")

if __name__ == "__main__":
    TeOSDesktop().mainloop()
