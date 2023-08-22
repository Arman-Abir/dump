from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser

file_path = None

def bg_color():
    color = colorchooser.askcolor()
    text.config(bg=color[1])

def foreground_color():
    color = colorchooser.askcolor()
    text.config(foreground=color[1])

def openfile():
    global file_path
    file_path = filedialog.askopenfilename(initialdir="C:\\", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete("1.0", END)
            text.insert(END, content)

def savefile():
    global file_path
    if file_path is None:
        file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file_text = text.get("1.0", END)
            file.write(file_text)

def copy():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())

def cut():
    copy()
    text.delete("sel.first", "sel.last")

def paste():
    text.insert(INSERT, text.clipboard_get())

window = Tk()
text = Text(window)
text.config(font=("Aerial",32))
menubar = Menu(window)
window.config(menu=menubar)

# File menu
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

# Edit menu
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Paste", command=paste)

# Format menu
formatmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Format", menu=formatmenu)
formatmenu.add_command(label="Background Color", command=bg_color)
formatmenu.add_command(label="Foreground Color", command=foreground_color)

window.geometry("400x450")
window.title("Notepad")
text.place (x=0, y=0, relwidth=1, relheight=1)
window.mainloop()
