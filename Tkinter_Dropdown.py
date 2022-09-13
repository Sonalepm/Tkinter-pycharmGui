from tkinter import *

root = Tk()


def dropdown(m):
    print(m)


msg = ["New File", "File opened", "File Saved", "Recent file opened", "Project closed", "Undo", "Redo", "Cut", "Copy",
       "Paste", "Delete", "Tool Windows", "Appearance", "Quick Definition", "Parameter Window", "Toolbar", "Customize",
       "Back", "Search", "Class", "File", "Symbol", "Line:Column", "Generate", "Code Completion", "Inspect Code",
       "Code Cleanup", "Analyze Code", "Analyze stack trace"]
myMenu = Menu(root)
root.config(menu=myMenu)

submenu1 = Menu(myMenu)
myMenu.add_cascade(label="File", menu=submenu1)
submenu1.add_command(label="New", command=lambda: dropdown(msg[0]))
submenu1.add_command(label="Open", command=lambda: dropdown(msg[1]))
submenu1.add_separator()
submenu1.add_command(label="Save As", command=lambda: dropdown(msg[2]))
submenu1.add_command(label="Open Recent", command=lambda: dropdown(msg[3]))
submenu1.add_separator()
submenu1.add_command(label="Close Project", command=lambda: dropdown(msg[4]))
submenu1.add_command(label="Exit", command=root.quit)

submenu2 = Menu(myMenu)
myMenu.add_cascade(label="Edit", menu=submenu2)
submenu2.add_command(label="Undo", command=lambda: dropdown(msg[5]))
submenu2.add_command(label="Redo", command=lambda: dropdown(msg[6]))
submenu2.add_separator()
submenu2.add_command(label="Cut", command=lambda: dropdown(msg[7]))
submenu2.add_command(label="Copy", command=lambda: dropdown(msg[8]))
submenu2.add_separator()
submenu2.add_command(label="Paste", command=lambda: dropdown(msg[9]))
submenu2.add_command(label="Delete", command=lambda: dropdown(msg[10]))

submenu3 = Menu(myMenu)
myMenu.add_cascade(label="View", menu=submenu3)
submenu3.add_command(label="Tool Windows", command=lambda: dropdown(msg[11]))
submenu3.add_command(label="Appearance", command=lambda: dropdown(msg[12]))
submenu3.add_separator()
submenu3.add_command(label="Quick Definition", command=lambda: dropdown(msg[13]))
submenu3.add_command(label="Parameter Window", command=lambda: dropdown(msg[14]))
submenu3.add_separator()
submenu3.add_command(label="Toolbar", command=lambda: dropdown(msg[15]))
submenu3.add_command(label="Customize", command=lambda: dropdown(msg[16]))

submenu4 = Menu(myMenu)
myMenu.add_cascade(label="Navigate", menu=submenu4)
submenu4.add_command(label="Back", command=lambda: dropdown(msg[17]))
submenu4.add_command(label="Search Everywhere", command=lambda: dropdown(msg[18]))
submenu4.add_separator()
submenu4.add_command(label="Class", command=lambda: dropdown(msg[19]))
submenu4.add_command(label="File", command=lambda: dropdown(msg[20]))
submenu4.add_separator()
submenu4.add_command(label="Symbol", command=lambda: dropdown(msg[21]))
submenu4.add_command(label="Line:Column", command=lambda: dropdown(msg[22]))

submenu5 = Menu(myMenu)
myMenu.add_cascade(label="Code", menu=submenu5)
submenu5.add_command(label="Generate", command=lambda: dropdown(msg[23]))
submenu5.add_command(label="Code Completion", command=lambda: dropdown(msg[24]))
submenu5.add_separator()
submenu5.add_command(label="Inspect Code", command=lambda: dropdown(msg[25]))
submenu5.add_command(label="Code Cleanup", command=lambda: dropdown(msg[26]))
submenu5.add_separator()
submenu5.add_command(label="Analyze Code", command=lambda: dropdown(msg[27]))
submenu5.add_command(label="Analyze stack trace", command=lambda: dropdown(msg[28]))

toolbar=Frame(root,bg='light green')
button1=Button(toolbar,text="OK")
toolbar.pack(side=TOP,fill=X)
button1.pack(side=RIGHT,padx=5,pady=5)

statusbar=Label(root,bg='light yellow',text="Status Bar",bd=5,anchor=W)
statusbar.pack(side=BOTTOM)
root.mainloop()
