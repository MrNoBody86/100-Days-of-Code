from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"



 
# --------------------- Create New Flash Cards ------------------------ #

df = pd.read_csv("Day-30to39\\Day-31\\project-28-flash-card\\data\\german_words.csv")
word_list = df.to_dict(orient="records")

# def random_word():
#     canvas.config = word_list[random.randint(0,2999)]["German"]







# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card 📇")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="Day-30to39\\Day-31\\project-28-flash-card\\images\\card_front.png")
canvas.create_image(400,263,image=card_front)
lang_text = canvas.create_text(400,150,text="German",fill="black",font=("Ariel",40,"italic"))
word_text = canvas.create_text(400,263,text=word_list[random.randint(0,2999)]["German"],fill="black",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

# Buttons

right_img = PhotoImage(file="Day-30to39\\Day-31\\project-28-flash-card\\images\\right.png")
button_right = Button(image=right_img,highlightthickness=0)
button_right.grid(column=1,row=1)

wrong_img = PhotoImage(file="Day-30to39\\Day-31\\project-28-flash-card\\images\\wrong.png")
button_wrong = Button(image=wrong_img,highlightthickness=0)
button_wrong.grid(column=0,row=1)


window.mainloop()
