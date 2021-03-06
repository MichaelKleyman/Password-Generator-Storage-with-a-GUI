from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)


    final_password = "".join(password_list)
            #OR
    # for char in password_list:
    #     password += char
    # print(str(password))

    password_input.insert(0, final_password)
    pyperclip.copy(final_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    site = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_dict = {
        site : {
            "email" : email,
            "password" : password
        }
    }
    if len(site) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Please do not leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=site, message="Are the details entered ok to save?")
        if is_ok:
            try:
                with open("data.json","r") as data:
                    read_data = json.load(data)
                    read_data.update(new_dict)
            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(new_dict,data,indent=4)
            else:
                with open("data.json", "w") as data:
                    json.dump(read_data, data, indent=4)
            finally:
                    website_input.delete(0,END)
                    password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

def search():
    try:
        with open("data.json", "r") as data:
            current_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="", message="No Data File Found")
    else:
        if website_input.get() in current_data:
            email = current_data[website_input.get()]["email"]
            password = current_data[website_input.get()]["password"]
            messagebox.showinfo(title=website_input.get(), message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="", message=f"No details for {website_input.get()} exist.")

# ---------------------------- SEARCH ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60,pady=60)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", font=("Arial", 15))
website_label.grid(column=0,row=1)

email_username_label = Label(text="Email/Username: ", font=("Arial", 15))
email_username_label.grid(column=0,row=2)

password_label = Label(text="Password: ", font=("Arial", 15))
password_label.grid(column=0,row=3)

password_button = Button(text="Generate Password", highlightthickness=4, command=generate)
password_button.grid(column=2,row=3)

add_button = Button(text="Add", width=36, highlightthickness=4, command=save)
add_button.grid(column=1,row=4, columnspan=2)

search_button = Button(text="Search", width=13, highlightthickness=4, command=search)
search_button.grid(column=2, row=1)

website_input = Entry(width=20)
website_input.focus()
website_input.grid(column=1,row=1)

email_username_input = Entry(width=35)
email_username_input.insert(END, "michaelkleyman99@gmail.com")
email_username_input.grid(column=1,row=2,columnspan=2)

password_input = Entry(width=21)
password_input.grid(column=1,row=3)

window.mainloop()