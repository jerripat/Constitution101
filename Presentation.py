
import sqlite3
import tkinter as tk
from tkinter import ttk

class GetPresidents:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Presidents")
        self.root.geometry("600x500")
        self.root.configure(background="#152e7a")

        self.my_label = ttk.Label(self.root, text="The Presidents", font=("Arial", 20), background="#152e7a", foreground="#dbac35")
        self.my_label.pack(pady=30)

        self.cbo = ttk.Combobox(self.root, font=("Arial", 14),values=[],width=30)
        self.cbo.pack(pady=30)

        self.data_label = ttk.Label(self.root, text='Data', font=("Arial", 12),background="#152e7a", foreground="#dbac35")
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
        self.data_label.config(text=(f'President #: {data}'))

if __name__ == "__main__":
    app = GetPresidents()
