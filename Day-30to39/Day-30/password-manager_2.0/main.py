from tkinter import Tk,END,Canvas,PhotoImage,Label,Entry,Button
from tkinter import messagebox
from random import choice,randint,shuffle
import json
import pyperclip

FILE_PATH = "Day-30to39\\Day-30\\password-manager_2.0\\data.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
                  'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                    'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try :
        with open(FILE_PATH,encoding="utf-8",mode= "r") as data_file:
            #Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="FileNotFoundError", message="No Data File Found.")
    else :
        for item in data :
            if website == item.key :
                messagebox.showinfo(title= website, message=f"These are the details entered: \nEmail: {item['email']} "
                                                      f"\nPassword: {item['password']} ")





# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website :{
            "email":email,
            "password":password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try :
            with open(FILE_PATH,encoding="utf-8",mode= "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open(FILE_PATH,encoding="utf-8",mode= "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file,indent=4)
        else :
            #Updating old data with new data
            data.update(new_data)

            with open(FILE_PATH,encoding="utf-8",mode= "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager 🔑")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
mypass_img = PhotoImage(file="Day-20to29\\Day-29\\project-27-password-manager\\logo.png")
canvas.create_image(100,100,image=mypass_img)
canvas.grid(column=1,row=0)

# Labels

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

# Entry

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=0,row=1,columnspan=3)

email_entry = Entry(width=35)
email_entry.insert(0,"ayushchauksey08@gmail.com")
email_entry.grid(column=1,row=2,columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=0,row=3,columnspan=3)

#Button

password_button = Button(text="Generate Password",width=14,command=generate_password)
password_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

search_button = Button(text="Search",width=14)
search_button.grid(column=2,row=1)
window.mainloop()
