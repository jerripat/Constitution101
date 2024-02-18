import tkinter as tk
from tkinter import *
root = tk.Tk()
root.geometry("400x400")
root.title("History of the United States Constitution")
root.configure(bg="#0b2266")


def fake():
    pass


def main_window() -> object:

    root = Tk()
    root.geometry("400x400")
    root.title("Summary of the United States Constitution, How it came to be. ")
    root.configure(background="#152e7a")
    main_label = tk.Label(root, text="Summary of The Constitution of The United States", background="#152e7a", foreground='gold', font=("Arial", 20))
    main_label.pack(pady=50)




    textbox = Text(root, wrap="word", font=("Arial", 12))
    textbox.pack(fill="both", expand=True, padx=10, pady=10)


if __name__ == "__Main_Window__":
    main_window()


root.mainloop()