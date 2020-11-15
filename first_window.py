from tkinter import *
from tkinter import messagebox
import tkinter.ttk
from game import Game

class First_Window:
    def __init__(self, colors, mensch, users):
        self.users = users
        self.mensch = mensch
        self.root = Tk()
        self.root.title('Login')
        self.root.geometry("225x150")

        self.username = Label(self.root, text='username:', width=10, pady=10)
        self.password = Label(self.root, text='password:', width=10)
        self.color = Label(self.root, text='color:', width=10, pady=10)
        self.username.grid(row=1, column=0)
        self.password.grid(row=2, column=0)
        self.color.grid(row=3, column=0)

        self.user_input = Entry(self.root)
        self.pass_input = Entry(self.root, show="*")
        self.user_input.grid(row=1, column=1, ipady=1)
        self.pass_input.grid(row=2, column=1, ipady=1)

        self.colors = colors
        self.color_menu = tkinter.ttk.Combobox(self.root, values=self.colors, width=17)
        self.color_menu.set(self.colors[0])
        self.color_menu.grid(row=3, column=1)

        self.login = Button(self.root, text='login', width=10)
        self.login.grid(row=4, column=1)

        self.login['command'] = self.check
        self.usr = ''

        # self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def check(self):
        with open('database.txt') as f:
            s = f.read()
        self.usr = self.user_input.get()
        pasw = self.pass_input.get()
        clr = self.color_menu.get()
        if self.usr in self.users:
            print("This user logged in before!")
            messagebox.showwarning("Login", "This user logged in before!")
        elif clr not in self.colors:
            print("Select a color")
            messagebox.showwarning("Login", "Select a color")
        elif clr in self.colors:
            for ln in s.split('\n'):
                if self.usr == ln.split()[0] and pasw == ln.split()[1]:
                    self.colors.remove(clr)
                    self.mensch.add_player(clr)
                    self.root.quit()
                    self.root.destroy()
                    break
            else:
                messagebox.showerror("Login", "Wrong username or password")
                print("Wrong username or password")
