
from tkinter import *
import Presentation
from Main_Window import main_window

class SplashScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Welcome")
        self.master.geometry("400x355")
        self.master.configure(background="#152e7a")
        self.image_path = "images/fullStack01.png"
        self.splash_image = PhotoImage(file=self.image_path)

        # Display the image using a Label widget
        self.image_label = Label(self.master, image=self.splash_image)
        self.image_label.place(relx=.5,rely=2.5,anchor='s')

        # Schedule the close_splash_and_open_main function to be called after 3000 milliseconds (3 seconds)
        self.master.after(3000, self.close_splash_and_open_main)

    def close_splash_and_open_main(self):
        # Close the splash window
        self.master.destroy()

        # Open the main window
        main_window = Tk()
        main_window.title("Welcome to the Constitution")
        main_window.geometry("500x400")
        main_window.configure(background="#152e7a")

        my_menu = Menu(main_window)  # Create menu for main window
        main_window.config(menu=my_menu)

        def open_presidents():
            # Open the presentations window
            Presentation.GetPresidents()
            main_window.destroy()

        def summary():
            pass

        file_menu = Menu(my_menu)
        my_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Presidents", command=open_presidents)
        file_menu.add_command(label="Constitution", command=summary)
        # file_menu.add_command(label="Summary", command=summary)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)

        main_window.mainloop()

# Create the main Tkinter window for the splash screen
root = Tk()
splash = SplashScreen(root)
root.mainloop()
