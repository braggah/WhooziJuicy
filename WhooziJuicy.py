#..............................................................................................
# Name: WhooziJuicy App
# Purpose :For Junior Software position abilities assessment
# Author: Mudau Glen
# Created: 04/04/2016
# Copyright: (c) Glen Mudau 2016

#.......................................................................................................

from tkinter import *
import tkinter.messagebox


class Person:


    def __init__(self, master):

        self.userName = StringVar()
        self.ageUser = IntVar()

        self.master = master
        master.title("The WhooziJuicy App")
        master.geometry('400x200+100+200')

        self.label1 = Label(master, text='Hello, and Welcome to WhooziJuicy Night Club ', fg="blue").grid(row=0, column=1)
        self.label2 = Label(master, text="Enter Username").grid(row=2, column=0)
        self.label2 = Label(master, text="Enter Age (remove 0 first)").grid(row=3, column=0)

        self.usernameTextbox = Entry(master, textvariable=self.userName).grid(row=2, column=1)
        self.ageTextbox = Entry(master, textvariable=self.ageUser).grid(row=3, column=1)

        self.checkAgeButton = Button(master, text="Check entry status", command=self.checkAge).grid(row=4, column=1)
        self.checkUserButton = Button(master, text="Check True age", fg="red", command=self.checkUser).grid(row=4, column=0)


    def checkUser(self):
        self.username = self.userName.get()
        if self.username == "Q24":
            X = 24 + 6
            return tkinter.messagebox.showinfo("Q24 True age", X)
        else:
            return tkinter.messagebox.showinfo("User", "Telling the truth")


    def checkAge(self):

        self.username = self.userName.get()
        self.age = self.ageUser.get()

        if self.age >= 18:
            if self.age < 90:
                if self.age <= 50:
                    return tkinter.messagebox.showinfo(self.username, "Acess Granted but Must stand on the Queue")
                else:
                    return tkinter.messagebox.showinfo(self.username, "Acess Granted, Is an elder, Must get in First")
            else:
                return tkinter.messagebox.showinfo(self.username, "Is Denied Acess, too old")

        elif self.age < 0:
            return tkinter.messagebox.showinfo(self.username, "Has entered invalid age")

        else:
            return tkinter.messagebox.showinfo(self.username, "Is under age!, and Denied Access")


root = Tk()
User = Person(root)
root.mainloop()








