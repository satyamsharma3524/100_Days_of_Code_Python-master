import json
import tkinter
from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip


# password generator

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


#  function definition
def save():
    web_entry = website_entry.get()
    website_entry.delete(0, END)
    mail_entry = email_entry.get()
    email_entry.delete(0, END)
    password = password_entry.get()
    password_entry.delete(0, END)

    new_entry = {
        web_entry.lower(): {
            "Email": mail_entry,
            "Password": password,
        }
    }

    if len(web_entry) == 0 or len(mail_entry) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please Enter some Data to Save.")
    else:
        try:
            with open("data.json", "r") as data:
                # reading from json file about old data
                new_data = json.load(data)
                # updating the old data with new data
                new_data.update(new_entry)

            with open('data.json', "w") as data:
                json.dump(new_data, data, indent=4)
                # json_data = json.load(data)
                # print(json_data)

        except FileNotFoundError:
            file = open("data.json", "w")
            json.dump(new_entry, file, indent=4)
            file.close()

        messagebox.showinfo(title="Save Success", message="Your data is saved successfully.")


def search_password():
    with open("data.json", "r") as data:
        all_data = json.load(data)
        try:
            searched_website = all_data[website_entry.get()]
            messagebox.showinfo(title="Search Result", message=f"Your {website_entry.get()} information is : \n\nEmail : {searched_website['Email']}\nPassword : {searched_website['Password']}")
        except KeyError:
            messagebox.showwarning(title="Invalid Entry", message=f"No Details for {website_entry.get()} :\n\nThe Website you entered is not available.")


# UI program
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="password_manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=53)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "satyam@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")
# website search button
search = Button(text="Search", width=14, command=search_password)
search.grid(row=1, column=2, sticky="w")

window.mainloop()
