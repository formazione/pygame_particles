import tkinter as tk
import tkinter.ttk as ttk
import os


def cat():
	os.startfile("snow_cat.pyw")


def living():
	os.startfile("snow5.pyw")


def foto():
	os.startfile("snow_foto.pyw")


def all_of_them():
	cat()
	living()
	foto()


def configure_style(
		style_type="azure",
		path="azure dark 2/azure dark.tcl"):
	print(os.getcwd())
	azure_style = ttk.Style(root)
	root.tk.call('source', path)
	azure_style.theme_use(style_type)


def choose(col, row):
	ttk.Label().grid(column=1, row=row - 1)
	ttk.Label(root, text="__________CHOOSE_____________").grid(column=col, row=row)


root = tk.Tk()
root.title("Choose your scene")
root.geometry("400x300")
configure_style()


ttk.Label(root, text="ANIMATION WITH PARTICLES").grid(column=0, row=0, columnspan=2, sticky="nswe")

choose(0,2)
ttk.Button(root,
	text="Snowing from living room",
	command=living,
	style="Accentbutton").grid(column=2, row=2, sticky="nswe")

choose(0, 4)
ttk.Button(root, text="Cat staring at rain", command=cat,
	style="Accentbutton").grid(column=2, row=4, sticky="w")


choose(0, 6)
ttk.Button(root, text="Foto", command=foto,
	style="Accentbutton").grid(column=2, row=6, sticky="w")


choose(0, 8)
ttk.Button(root, text="Launch all", command=all_of_them,
	style="Accentbutton").grid(column=2, row=8, sticky="w")


root.mainloop()