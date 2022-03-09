import tkinter

window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(width=500, height=500)

my_label = tkinter.Label(text="This is my label", font=("arial", 24, "bold"))
my_label.pack()

window.mainloop()
