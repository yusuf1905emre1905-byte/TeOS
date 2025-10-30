from apps.user_tv import UserTV
from apps.tpk_creator import TPKCreator
from system.power import PowerSystem

def open_usertv(): UserTV(root)
def open_tpk(): TPKCreator(root)
battery_label = tk.Label(root, text="🔋100%", bg="#111", fg="lime")
battery_label.pack(side="top")
power = PowerSystem(battery_label)
