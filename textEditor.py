from tkinter import *
from tkinter.filedialog import *
import sys
import os


fileName = None
BG = "#1e1e1e"
FG = "#d4d4d4"
CURSOR = "#ffffff"
MENU_BG = "#2d2d2d"


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def updateTitle():
    if fileName is None:
        root.title("Come's Blog - Sin Título")
    else:
        root.title(f"Come's Blog - {os.path.basename(fileName)}")

def newFile():
    global fileName
    fileName = None
    text.delete(1.0, END)
    updateTitle()

def saveFile():
    global fileName
    if fileName is None:
        saveAs()
        return
    t= text.get(1.0,END)
    with open(fileName, "w") as f:
        f.write(t)
    updateTitle()

def saveAs():
    global fileName
    f = asksaveasfile(mode='w', defaultextension='.txt')
    if f is None:
        return

    t = text.get(1.0,END)
    f.write(t.rstrip())

    fileName = f.name
    f.close()
    updateTitle()

def openFile():
    global fileName
    f = askopenfile(mode='r')
    if f is None:
        return
    t = f.read()
    text.delete(1.0, END)
    text.insert(1.0, t) 
    fileName = f.name  
    f.close()
    updateTitle()

def undo():
    try:
        text.edit_undo()
    except:
        pass

def redo():
    try:
        text.edit_redo()
    except:
        pass

#Configuraciones del root
root = Tk()
icon_path = resource_path("odin.png")
root.iconphoto(False, PhotoImage(file=icon_path))
root.title("Come's Blog - Sin Título")
root.geometry("700x500")
root.minsize(width=400, height=400)
root.resizable(True, True)
root.bind("<Control-s>", lambda e: saveFile())
root.bind("<Control-o>", lambda e: openFile())
root.bind("<Control-n>", lambda e: newFile())
root.bind("<Control-z>", lambda e: undo())
root.bind("<Control-p>", lambda e: redo())

#Configuraciones del scroll vertical
scroll_y = Scrollbar(root)
scroll_y.pack(side= RIGHT, fill = Y)

#Configuracion del scroll horizontal
scroll_x = Scrollbar(root, orient=HORIZONTAL)
scroll_x.pack(side=BOTTOM, fill=X)

text = Text(
    root,
    yscrollcommand = scroll_y.set,
    xscrollcommand=scroll_x.set,
    wrap="none",
    bg=BG,
    fg=FG,
    insertbackground=CURSOR,
    undo=True,
)
text.pack(expand=True, fill="both")

scroll_y.config(command=text.yview)
scroll_x.config(command=text.xview)


#Configuracion de menu de la ventana
menubar = Menu(root, bg=MENU_BG, fg=FG)
filemenu = Menu(menubar, tearoff=0, bg=MENU_BG, fg=FG)

filemenu.add_command(label="Nuevo", command=newFile)
filemenu.add_command(label="Abrir", command=openFile)
filemenu.add_command(label="Guardar", command=saveFile)
filemenu.add_command(label="Guardar como...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Deshacer", command=undo)
filemenu.add_command(label="Rehacer", command=redo)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu = (filemenu))

root.config(menu=menubar)
root.mainloop()