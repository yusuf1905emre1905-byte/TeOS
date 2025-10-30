import tkinter as tk

class TeKeyboard(tk.Toplevel):
    def __init__(self, parent, text_widget):
        super().__init__(parent)
        self.title("Free TeOS Keyboard")
        self.geometry("700x250")
        self.config(bg="#222")
        self.text_widget = text_widget

        # özel klavye düzeni (örnek: A → 8, B → 7, C → *)
        layout = [
            ["A","B","C","D","E","F","G","H","I","J"],
            ["K","L","M","N","O","P","Q","R","S","T"],
            ["U","V","W","X","Y","Z","SPACE","BACK","ENTER"]
        ]

        self.keymap = {
            "A":"8","B":"7","C":"*","D":"(","E":")","F":"!","G":"@","H":"#",
            "I":"$","J":"%","K":"^","L":"&","M":"_","N":"=","O":"+","P":"-",
            "Q":"/","R":"<","S":">","T":"?","U":"[","V":"]","W":"{","X":"}",
            "Y":"|","Z":"~"
        }

        for r,row in enumerate(layout):
            for c,key in enumerate(row):
                tk.Button(self, text=key, width=6, height=2,
                          command=lambda k=key:self.press(k),
                          bg="#333", fg="white").grid(row=r, column=c, padx=2, pady=2)

    def press(self, key):
        if key=="SPACE":
            self.text_widget.insert(tk.END, " ")
        elif key=="BACK":
            self.text_widget.delete("end-2c")
        elif key=="ENTER":
            self.text_widget.insert(tk.END, "\n")
        else:
            mapped=self.keymap.get(key,key)
            self.text_widget.insert(tk.END, mapped)
          from gui.keyboard import TeKeyboard

def open_keyboard():
    TeKeyboard(root, text_box)
  
