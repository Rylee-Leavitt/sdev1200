#
# Rylee Leavitt
# 5/2/2025
# Name and Address Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program.  
# The code below was auto-generated. 
# Delete unnecessary code.

#Main.py

import tkinter as tk

class MyGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.title("Name and Address")
        self.main_window.geometry("300x300")

        # Create the string variable objects to display name, street, and city-state-zip
        self.name_value = tk.StringVar()
        self.street_value = tk.StringVar()
        self.csz_value = tk.StringVar()

        # Create two frames
        self.info_frame = tk.Frame(self.main_window)
        self.button_frame = tk.Frame(self.main_window)

        # Create label widgets associated with the StringVar objects
        self.name_label = tk.Label(self.info_frame, textvariable=self.name_value)
        self.street_label = tk.Label(self.info_frame, textvariable=self.street_value)
        self.csz_label = tk.Label(self.info_frame, textvariable=self.csz_value)

        # Pack the labels
        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()

        # Create button widgets
        self.show_info_button = tk.Button(self.button_frame, text='Show Info', command=self.show)
        self.quit_button = tk.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        # Pack the buttons
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

        # Pack the frames
        self.info_frame.pack()
        self.button_frame.pack()

    # Define the callback function for the "Show Info" button
    def show(self):
        self.name_value.set('Rylee Leavitt')
        self.street_value.set('2600 College Drive')
        self.csz_value.set('Rock Springs, WY, 82901')  # Fixed typo (csv -> csz)

# Create an instance of MyGUI class
my_gui = MyGUI()

# Enter the main Tkinter loop
tk.mainloop()