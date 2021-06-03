from tkinter import *
from tkinter import messagebox


# initialising the root
root = Tk()
root.title('Log In')
root.geometry('350x400')
root.config(bg='#DDFFF7')

# labels
lb1 = Label(root, text="Username")
lb1.place(x=0, y=0)
lb1.config(bg='#DDFFF7')
lb2 = Label(root, text="Password")
lb2.place(x=0, y=50)
lb2.config(bg='#DDFFF7')

# entries
entry1 = Entry(root)
entry1.place(x=180, y=0)
entry1.config(bg='#00AACC', fg='#B7094C')
entry2 = Entry(root)
entry2.place(x=180, y=50)
entry2.config(bg='#00AACC', fg='#B7094C')


user_pass = {'Jayden': 'jaydenmay', 'Brent Lee': 'yourstepbro', 'Jason': 'faketaxi@17',
             'Yamkela': 'breadislife'}


def user_pass_search():
    if entry1.get() in user_pass:
        if entry2.get() == user_pass[entry1.get()]:
            root.destroy()
            import excursion
        else:
            messagebox.showerror(message="Username and password does not match")
    else:
        messagebox.showerror(message="Username does not exist")


def delete():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')


# buttons
btn1 = Button(root, text="Verify", command=user_pass_search)
btn1.place(x=0, y=150)
btn1.config(bg='#B7094C', fg='#DDFFF7')
btn2 = Button(root, text="Clear", command=delete)
btn2.place(x=100, y=150)
btn2.config(bg='#B7094C', fg='#DDFFF7')
btn3 = Button(root, text="Exit", command="exit")
btn3.place(x=200, y=150)
btn3.config(bg='#B7094C', fg='#DDFFF7')


root.mainloop()
