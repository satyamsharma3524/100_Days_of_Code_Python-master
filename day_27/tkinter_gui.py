import tkinter

window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(width=500, height=500)

# label
my_label = tkinter.Label(text="This is my label", font=("arial", 24, "bold"))
my_label.pack()
my_label.config(padx=10, pady=10)

# entry
user_input = tkinter.Entry(width=50)
user_input.pack()


# button
def button_click():
    my_label["text"] = user_input.get()


button = tkinter.Button(text="Click Me", command=button_click)
button.pack()
button.config(padx=10, pady=10)

window.mainloop()
