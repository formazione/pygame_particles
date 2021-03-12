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
        # Need to have this: 
        path="azure dark 2/azure dark.tcl"):
    "Use the new style for tkinter"
    print(os.getcwd())
    azure_style = ttk.Style(root)
    root.tk.call('source', path)
    azure_style.theme_use(style_type)


def choose(col, row):
    "Just to write choose in tkinter window"
    ttk.Label().grid(column=1, row=row - 1)
    ttk.Label(root, text="__________CHOOSE_____________").grid(column=col, row=row)

def toggle_fullscreen(event=None):
    "bind to f11 and Escape to toggle fullscreen mode"
    root.state = not root.state  # Just toggling the boolean
    root.attributes("-fullscreen", root.state)
    return "break"

def toggle_geom(event):
    "This expand the window"
    global root
    
    geom = root.winfo_geometry()
    print(geom, root._geom)
    root.geometry(root._geom)
    root._geom = geom

pad = 3
# self.tk.bind("<Escape>", self.end_fullscreen)
root = tk.Tk()
root.geometry("400x300")
root.title("Choose your scene")
root._geom = "400x300+0+0"
# w = root.winfo_screenwidth()
# h = root.winfo_screenheight()
# root.geometry(f"{w}x{h}")
root.bind("<F11>", toggle_fullscreen)
root.bind('<Escape>', toggle_fullscreen)
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