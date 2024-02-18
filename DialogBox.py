
from tkinter import *
from tkinter import filedialog

class App(Tk):

    def __init__(self):
        super().__init__()

        self.title("Tkinter.com - OOP File Dialog")
        self.geometry("700x450")

        self.my_text = Text(self, width=80, height=20)
        self.my_text.pack(pady=30)
        self.my_button = Button(self, text="Open File", command=self.file)
        self.my_button.pack(pady=10)

    def file(self):

        self.my_file = filedialog.askopenfilename(initialdir="", title="Select a file",
                                                  filetypes=(("Text Files", "*.txt"),
                                                             ("All Files", "*.*")))
        if self.my_file:
            with open(self.my_file, 'r') as file:
                self.my_text.delete(1.0, END)  # Clear previous text
                self.my_text.insert(END, file.read())

app = App()
app.mainloop()
