import tkinter

window = tkinter.Tk()

window.title("Mile to KM converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


# function definition
def convert():
    mile = float(user_input.get())
    mile *= 1.609
    output.config(text=mile)


# input entry
user_input = tkinter.Entry(width=10)
user_input.grid(row=0, column=1)

# text label
miles = tkinter.Label(text="Miles")
miles.grid(row=0, column=4)

# text label
equals = tkinter.Label(text="is Equal to")
equals.grid(row=3, column=0)

# output label
output = tkinter.Label(text="0")
output.grid(row=3, column=1)

# text label
kilometers = tkinter.Label(text="K.M.")
kilometers.grid(row=3, column=4)

# calculate button
calculate = tkinter.Button(text="Calculate", command=convert)
calculate.grid(row=4, column=1)

window.mainloop()
