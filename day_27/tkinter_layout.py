import tkinter

window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(width=500, height=500)


# function definition
def button_click():
    my_label["text"] = user_input.get()


# label
my_label = tkinter.Label(text="This is my label", font=("arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=120, y=100)
my_label.grid(row=0, column=0)

# entry
user_input = tkinter.Entry(width=50)
# user_input.pack()
user_input.grid(row=2, column=4)

# button1
button = tkinter.Button(text="Click Me", command=button_click)
# button.pack()
button.grid(row=1, column=2)

# button2
button = tkinter.Button(text="button2")
button.grid(row=0, column=3)
window.mainloop()
