from tkinter import Tk, Label, Button, FLAT, SOLID, RIGHT


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator by hilsCYBER")

        self.display = Label(width=25, relief=FLAT, fg="BLACK", bg="GREY", bd=1, justify=RIGHT, font="Lato 14")
        self.display.grid(columnspan=4, row=0)

        self.equals_button = Button(master, text="=", bg="BLACK", fg="BLUE", font="Lato 16", borderwidth=0, height=6,
                                    command=lambda button="=": self.button_action(button))
        self.equals_button.grid(column=4, row=1, rowspan=4)

        self.operations = [['7', '8', '9', '/'],
                           ['4', '5', '6', '*'],
                           ['1', '2', '3', '-'],
                           ['0', 'Del', '.', '+']]

        for i in range(len(self.operations)):
            for j in range(len(self.operations[i])):
                self.numpad = Button(master, text=self.operations[j][i], relief=SOLID, borderwidth=0, bg='BLACK',
                                     fg="BLUE", font="Lato 16", activeforeground="PURPLE", activebackground="GREEN",
                                     width=3, command=lambda button=self.operations[j][i]: self.button_action(button))
                self.numpad.grid(column=i, row=j + 1)

    def button_action(self, button_click):

        if button_click == "=":
            current_value = self.display.cget("text")
            try:
                result = eval(current_value)
                if result != "":
                    self.display.config(text=result)
            except:
                self.display.config(text=current_value)
        elif button_click == "Del":
            self.display.config(text=" ")
        else:
            current_value = self.display.cget("text")
            self.display.config(text=str(current_value) + button_click)


root = Tk()

root.resizable(0,0)
root.geometry("320x200")
root.configure(bg="GREY")
my_gui = Calculator(root)

root.mainloop()

