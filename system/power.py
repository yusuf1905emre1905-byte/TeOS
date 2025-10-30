import time
import threading
import tkinter as tk

class PowerSystem:
    def __init__(self, ui_label):
        self.level = 100
        self.charging = False
        self.ui_label = ui_label
        self.running = True
        threading.Thread(target=self.drain, daemon=True).start()

    def drain(self):
        while self.running:
            if not self.charging:
                self.level = max(0, self.level - 1)
            self.update_ui()
            time.sleep(10)

    def plug_in(self):
        self.charging = True
        threading.Thread(target=self.charge, daemon=True).start()

    def unplug(self):
        self.charging = False

    def charge(self):
        while self.charging and self.level < 100:
            self.level += 2
            self.update_ui()
            time.sleep(3)

    def update_ui(self):
        status = f"🔋 {self.level}% {'⚡' if self.charging else ''}"
        self.ui_label.config(text=status)
        from system.power import PowerSystem
battery_label = tk.Label(root, text="🔋100%", bg="#111", fg="lime")
battery_label.pack(side="top")
power = PowerSystem(battery_label)
