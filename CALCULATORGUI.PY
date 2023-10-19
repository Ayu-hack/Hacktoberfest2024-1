from tkinter import*

def calculator():
    def button_click(number):
        current = entry.get()
        entry.delete(0, END)
        entry.insert(0, current + str(number))

    def clear():
        entry.delete(0, END)

    def calculate():
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, END)
            entry.insert(0, result)
        except Exception as e:
            entry.delete(0, END)
            entry.insert(0, "Error")

   
    cal_win = Tk()
    cal_win.title("Calculator")

    
    entry = Entry(cal_win, width=40,font=("Arial",16))
    entry.grid(row=0, column=0, columnspan=4,ipady=30)

   
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
    ]

    for (text, row, col) in buttons:
        button = Button(cal_win, text=text, padx=20, pady=20, command=lambda t=text: button_click(t),font=("Arial",16),bd=2,fg="white",bg="grey")
        button.grid(row=row, column=col,pady=1)

    clear_button = Button(cal_win, text='C', padx=20, pady=20, command=clear,font=("Arial",16),bd=2,fg="white",bg="grey")
    clear_button.grid(row=5, column=1, columnspan=3)

    
    equal_button = Button(cal_win, text='=', padx=20, pady=20, command=calculate,font=("Arial",16),bd=2,fg="white",bg="grey")
    equal_button.grid(row=5, column=3)


    cal_win.mainloop()


calculator()