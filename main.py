from tkinter import *
import pandas
import random
import csv


def choose_random_french_word():
    words_file = pandas.read_csv("data/french_words.csv")

    french_words = words_file["French"]
    english_words = words_file["English"]

    french_words = french_words.tolist()
    english_words = english_words.tolist()
    # window.after_cancel(flip_timer)

    word_generated = random.choice(french_words)
    f_index = french_words.index(word_generated)
    # print(word_generated)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=word_generated, fill="black")

    window.after(3000, choose_random_english_word, f_index, english_words)


def choose_random_english_word(f_index, english_words):
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title, text="English", fill="white")
    corresponding_english_word = english_words[f_index]
    # print(corresponding_english_word)
    canvas.itemconfig(word, text=corresponding_english_word, fill="white")


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front_img)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))


right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, command=choose_random_french_word)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=choose_random_french_word)


right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

choose_random_french_word()

window.mainloop()


