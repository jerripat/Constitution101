from tkinter import *

def fake():
    pass

def close_splash_and_open_main():
    # Close the splash window
    splash_window.destroy()

    # Open the main window
    main_window = Tk()
    main_window.title("Welcome to the Constitution")
    main_window.geometry("400x400")
    main_window.configure(background="#152e7a")

    my_menu = Menu(main_window)  # Create menu for main window
    main_window.config(menu=my_menu)

    file_menu = Menu(my_menu)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=fake)
    file_menu.add_command(label="Open", command=fake)
    file_menu.add_command(label="Save", command=fake)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=quit)

    main_window.mainloop()


# Create the splash window
splash_window = Tk()
splash_window.title("Splash")
splash_window.geometry("400x400")
splash_window.configure(background="#152e7a")

# Schedule the close_splash_and_open_main function to be called after 3000 milliseconds (3 seconds)
splash_window.after(3000, close_splash_and_open_main)

# Load the image
image_path = "images/fullStack01.png"
splash_image = PhotoImage(file=image_path)

# Display the image using a Label widget
image_label = Label(splash_window, image=splash_image)
image_label.place(rely=.0018, relx=.5, anchor="n")

splash_window.mainloop()

