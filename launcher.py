import tkinter as tk
import os


def cat():
	os.startfile("snow_cat.py")

def living():
	os.startfile("snow5.py")

def foto():
	os.startfile("snow_foto.py")

root = tk.Tk()
tk.Button(root, text="Snowing from living room", command=living).pack()
tk.Button(root, text="Cat staring rain", command=cat).pack()
tk.Button(root, text="Foto", command=foto).pack()
root.mainloop()