from tkinter import *
import tkinter.messagebox
import sqlite3


root = Tk()
root.geometry("500x600")
root.title("Anmeldung")
root.configure(background="sky blue")
root.iconbitmap("book1.ico")
root.eval('tk::PlaceWindow . center')

bg = PhotoImage(file="re.png")
Label(root, image=bg, bg="sky blue", width=200, height=200).pack()

Label(root, text="Login", bg="sky blue", font=("Arial", 16)).pack()
t1 = Text(root, height=2, width=20)
t1.pack()

Label(root, text="Passwort", bg="sky blue", font=("Arial", 16)).pack()
t2 = Text(root, height=2, width=20)
t2.pack()

b2 = Button(root, text="OK", bg="#F0F0F8", font=("Arial", 16), command=lambda: input())
b2.pack(pady=10)

a = ""
b = ""
def input():
    a = t1.get(1.0, "end-1c")
    t1.delete(1.0, "end-1c")
    b = t2.get(1.0, "end-1c")
    t2.delete(1.0, "end-1c")
    conn = sqlite3.connect("login.db")

    cursor = conn.execute("SELECT * FROM Users WHERE Login =?", [a])
    result = str(cursor.fetchall()).translate({ord(i): None for i in "[]'(), "})

    if(result == a+b):
        tkinter.messagebox.showinfo(title="nice", message="Angemeldet!")
    else:
        tkinter.messagebox.showinfo(title="not nice", message="Gedächtnisprobleme?")

    conn.commit()
    conn.close()

def reg():
    win = Toplevel()
    win.geometry("300x400")
    win.title("Registrierung")
    win.configure(background="sky blue")
    win.iconbitmap("book1.ico")

    Label(win, text="Login", bg="sky blue", font=("Arial", 16)).pack()
    global t3
    t3 = Text(win, height=2, width=20)
    t3.pack()

    Label(win, text="Passwort", bg="sky blue", font=("Arial", 16)).pack()
    global t4
    t4 = Text(win, height=2, width=20)
    t4.pack()

    b3 = Button(win, text='OK', command=lambda:[input2(), quit()])
    b3.pack(pady=10)

    def quit():
        win.destroy()

c = ""
d = ""
def input2():
    c = t3.get("1.0", "end-1c")
    d = t4.get("1.0", "end-1c")
    conn = sqlite3.connect("login.db")

    cursor = conn.execute("SELECT Login FROM Users WHERE Login =?", [c])
    result3 = str(cursor.fetchall()).translate({ord(i): None for i in '[](),'})

    if(c in result3):
        tkinter.messagebox.showinfo(title="bad luck", message="Der Benutzername ist schon vergeben")
    else:
        conn.execute("INSERT INTO Users (Login, Passwort) \
                  VALUES ('{}', '{}')".format(c, d));
        conn.commit()
        conn.close()
        tkinter.messagebox.showinfo(title="nice", message="Registriert!")

Label(root, text="", bg="sky blue", font=("Arial", 16), height=1).pack()

l4 = Label(root, text="Neuer Benutzer? Registriere dich", bg="sky blue", font=("Arial", 16))
l4.pack(pady=10)
Button(root, height=2, width=10, font=("Arial", 16), text='Registrierung', command=reg).pack()


root.mainloop()