from tkinter import Tk, Text, Label
import tkinter as tk
from ttkbootstrap import *

import Presentation


def main_window():
    # Create the main window
    root = tk.Tk()
    root.geometry("800x600")
    root.title("History of the United States Constitution")
    root.configure(bg="#152e7a")

    # Create a label
    main_label = Label(root, text="The Constitution", font=("Arial", 20), bg = "#152e7a")
    main_label.pack(pady=10)
    textbox = Text(root, wrap="word", font=("Arial", 12), bg="#152e7a")
    textbox.pack(fill="both", expand=True, padx=10, pady=10)

    # Insert the provided text into the textbox with single spacing
    constitution_text = """The United States Constitution emerged from the Philadelphia Convention in 1787, 
            where delegates from 12 states (Rhode Island abstained) deliberated over the weaknesses of the 
            Articles of Confederation. Led by figures like James Madison and Alexander Hamilton, 
            the convention drafted the Constitution, establishing the framework for the federal government. 
            The document faced opposition from Anti-Federalists who feared centralized power. 
            To address concerns, Federalists like Madison, Hamilton, and John Jay penned a series of essays 
            known as the Federalist Papers, advocating for the Constitution's ratification. After intense 
            debates in state ratifying conventions, the Constitution was ratified on June 21, 1788. 
                Amid concerns about individual liberties, the first ten amendments, collectively known as the 
            Bill of Rights, were added to the Constitution in 1791. These amendments protected fundamental 
            rights such as freedom of speech, religion, and the right to a fair trial, mollifying Anti-Federalist 
            concerns. The Constitution was expanded in 1789 to include the amendments to The Constitution evolved 
            as the nation expanded territorially and grappled with profound moral questions. Issues like states' 
            rights versus federal authority escalated tensions, culminating in the Civil War. The conflict led 
            to significant amendments, including the abolition of slavery thirteenth Amendment and granting 
            equal protection under the law fourteenth Amendment. 
                The Constitution was expanded in 1890 to include the amendments to the Constitution The early 
            twentieth century saw a wave of reforms aimed at addressing societal injustices and enhancing democracy. 
            Progressive movements led to constitutional amendments such as women's suffrage (Nineteenth Amendment) 
            and the establishment of an income tax (Sixteenth Amendment). 
                The Constitution continues to adapt to contemporary challenges and interpretations. 
            Landmark Supreme Court cases have shaped its meaning, from Brown v. Board of Education (1954) 
            desegregating schools to Roe v. Wade (1973) affirming abortion rights."""

    textbox.insert("1.0", constitution_text)

main_window()
#Presentation.GetPresidents()

ttk.root.mainloop()
