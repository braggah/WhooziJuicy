from tkinter import *
import tkinter.messagebox

class Person:

    def __init__(self, form):
        frame = Frame(form)
        frame.pack()

        self.checkAgeButton = Button(frame, text="Entry Status", command=self.checkAge())
        self.checkAgeButton.pack(side=RIGHT)
        self.checkUsername = Button(frame, text="Check user", command=self.checkuser())
        self.checkAgeButton.pack(side=RIGHT)
        self.quitButton = Button(frame, text="Exit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def checkAge(self):
        username = input("Enter username: ")
        age = int(input("Enter age: "))
        if age >= 18:
            print(username, "Is granted access and")
            if age < 90:
                if age <= 50:
                    print(username, "Must stand on que")
                else:
                    print(username, "Must get in first")
            else:
                print(username, "Is denied access!, too old/Invalid")

        elif age < 0:
            print(username, "Has entered invalid age")

        else:
            tkinter.messagebox.showinfo(username, "Is denied access - (Under Age)")

    def checkuser(self, X):
        if username == "Q24":
            self.X = 24 + 6
            return int(self.X)

root = Tk()
tkinter.messagebox.showinfo("WhooziJuicy App")
thePerson = Person(root)
root.mainloop()




