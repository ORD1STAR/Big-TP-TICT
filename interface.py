import tkinter as tk
import os

#Configuration de la fenetre
window = tk.Tk()
window.title("BigTp")
window.geometry("500x500+350+50")
window.config(bg="#333")
# titre
tk.Label(window, text="Big Tp TICT", bg="#444", fg="#fff",font=("Arial", 24), padx=20, pady=10).pack()

#suppression de la 1ere fenetre et ouverture de la nouvelle fenetre
def tp1():
    window.destroy()
    os.system("py BT1.py")

#bouton pour ouvrire le BIG TP 1
tk.Button(window, text="TP1", bg="#444", fg="#fff",font=("Arial", 24), padx=20, pady=10, command=tp1).pack(pady=30)

window.mainloop()