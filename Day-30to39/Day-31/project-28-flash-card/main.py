from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
flip_timer = None
word_list = {}


# --------------------- Create New Flash Cards ------------------------ #

try :
    data = pd.read_csv("Day-30to39\\Day-31\\project-28-flash-card\\data\\words_to_learn.csv")
except FileNotFoundError :
    original_data = pd.read_csv("Day-30to39\\Day-31\\project-28-flash-card\\data\\german_words.csv")
    word_list = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")

def next_card():
    """Generate random German Word"""
    global current_card , flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_list)
    canvas.itemconfig(word_text,text = current_card["German"],fill = "black")
    canvas.itemconfig(lang_text,text = "German",fill = "black")
    canvas.itemconfig(canvas_image,image = card_front)
    flip_timer = window.after(3000, func=flip_card)

def known_word():
    word_list.remove(current_card)
    df = pd.DataFrame(word_list)
    df.to_csv("Day-30to39\\Day-31\\project-28-flash-card\\data\\words_to_learn.csv",index=False)
    next_card()



# ------------------- English Translation in 3s ----------------------- #

def flip_card():
    canvas.itemconfig(canvas_image,image = card_back)
    canvas.itemconfig(lang_text,text = "English",fill = "white")
    canvas.itemconfig(word_text,text = current_card["English"],fill = "white")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card 📇")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,flip_card)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="Day-30to39\\Day-31\\project-28-flash-card\\images\\card_front.png")
card_back = PhotoImage(file="Day-30to39\\Day-31\\project-28-flash-card\\images\\card_back.png")
canvas_image = canvas.create_image(400,263,image=card_front)
lang_text = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
word_text = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

# Buttons

right_img = PhotoImage(file="Day-30to39\\Day-31\\project-28-flash-card\\images\\right.png")
button_right = Button(image=right_img,highlightthickness=0,command=known_word)
button_right.grid(column=1,row=1)

wrong_img = PhotoImage(file="Day-30to39\\Day-31\\project-28-flash-card\\images\\wrong.png")
button_wrong = Button(image=wrong_img,highlightthickness=0,command=next_card)
button_wrong.grid(column=0,row=1)

next_card()

window.mainloop()
