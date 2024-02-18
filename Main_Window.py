import tkinter as tk
from tkinter import *

def main_window():
    root = Tk()
    root.geometry("400x400")
    root.title("Summary of the United States Constitution, How it came to be.")
    root.configure(background="#152e7a")
    main_label = Label(root, text="Summary of The Constitution of The United States", background="#152e7a", foreground='gold', font=("Arial", 20))
    main_label.pack(pady=50)

    image_path = "images/fullStack01_small.png"
    splash_image = PhotoImage(file=image_path)
    image_label = Label(root, image=splash_image)
    image_label.place(rely=.0018, relx=.5, anchor="n")

    textbox = Text(root, wrap="word", font=("Arial", 12))
    textbox.pack(fill="both", expand=True, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_window()
