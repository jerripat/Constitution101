import sqlite3
import tkinter as tk
from tkinter import ttk, END, Text


class GetPresidents:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Presidents")
        self.root.geometry("500x500")
        self.root.configure(bg="#152e7a")

        # Initialize main_menu and file_menu
        self.main_menu = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.main_menu, tearoff=0)

        self.main_menu.add_cascade(label="File", menu=self.file_menu)

        # Add commands to file_menu
        self.file_menu.add_command(label="Main Window", command=self.open_home)
        self.file_menu.add_command(label="Constitution", command=self.summary)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=quit)

        self.root.config(menu=self.main_menu)

        self.my_label = ttk.Label(self.root, text="The Presidents", font=("Arial", 20), background="#152e7a", foreground="#dbac35")
        self.my_label.pack(pady=30)

        self.cbo = ttk.Combobox(self.root, font=("Arial", 14), values=[], width=30)
        self.cbo.pack(pady=30)

        self.data_label = ttk.Label(self.root, text='Data', font=("Arial", 12), background="#152e7a", foreground="#dbac35")
        self.data_label.pack(pady=30)

        self.conn = sqlite3.connect("presidents.db")
        self.cursor = self.conn.cursor()

        self.presidents = []

        self.cursor.execute("SELECT * FROM Presidents")
        for pres in self.cursor.fetchall():
            self.presidents.append(pres[1])

        self.conn.close()

        self.cbo['values'] = self.presidents
        self.cbo.bind("<<ComboboxSelected>>", self.fetch_president_data)

        self.root.mainloop()

    def fetch_president_data(self, event):
        selected_president = self.cbo.get()
        self.conn = sqlite3.connect("presidents.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Presidents WHERE name=?", (selected_president,))
        data = self.cursor.fetchone()
        self.conn.close()
        self.my_label.config(text=f'You Selected {selected_president}')
        self.display_data(data)

    def display_data(self, data):
        self.my_text = Text(self.root, width=80, height=5, font=("Arial", 14, "bold"))
        self.my_text.pack(pady=30)
        self.my_text.delete(1.0, END)  # Clear previous text
        self.my_text.insert(END, data)

    def summary(self):
        pass

    def open_home(self):
        # You may define open_home method as a part of this class if needed
        pass


if __name__ == "__main__":
    app = GetPresidents()