from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

card_data = pandas.read_csv("flash-card-project-start/data/french_words.csv")
to_learn = card_data.to_dict(orient="records")
current_card = {}

def next_button():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)


# GUI
card_front_img = PhotoImage(file="flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(file="flash-card-project-start/images/card_back.png")
right_img = PhotoImage(file="flash-card-project-start/images/right.png")
wrong_img = PhotoImage(file="flash-card-project-start/images/wrong.png")
card_background = canvas.create_image(401, 266, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# O/X button
wrong_button = Button(padx=50, pady=50, highlightthickness=0, image=wrong_img, command=next_button)
wrong_button.grid(row=1, column=0)
right_button = Button(padx=50, pady=50, highlightthickness=0, image=right_img, command=next_button)
right_button.grid(row=1, column=1)

# card_text
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))









window.mainloop()