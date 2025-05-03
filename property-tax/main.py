#
# Rylee Leavitt
# 5/3/2025
# Property Tax Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program. 

#main.py

#Importing the Tkinter library for GUI functionality
#import tkinter as tk and import messagebox
import tkinter as tk
from tkinter import messagebox

#Calculate and display the assessment value and property tax
def calculate_tax():
    try:
        actual_value = float(entry_value.get())         #Get user input and convert to float
        assessment_value = actual_value * 0.6           #Calculate the assessment value (60% of actual value)
        property_tax = (assessment_value / 100) * 0.75  #Calculate property tax (0.75 per $100 of assessment value)
        
        #Update labels to display calculated values
        label_assessment.config(text=f"Assessment Value: ${assessment_value:.2f}")
        label_tax.config(text=f"Property Tax: ${property_tax:.2f}")
    
    # Show an error message if input is not a valid number
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number (with no commas/notation).")

# Create main window
root = tk.Tk()  # Initialize the main application window
root.title("Property Tax Calculator")  # Set window title

# Entry field for actual value
tk.Label(root, text="Enter Actual Value of Property ($):").pack(pady=5)  # Label for entry field
entry_value = tk.Entry(root)  # Create entry field for user input
entry_value.pack(pady=5)  # Display entry field with padding

# Button to calculate tax
tk.Button(root, text="Calculate", command=calculate_tax).pack(pady=5)  # Button to trigger tax calculation

# Labels to display results
label_assessment = tk.Label(root, text="Assessment Value: $0.00")  # Default label for assessment value
label_assessment.pack(pady=5)  # Display label with padding

label_tax = tk.Label(root, text="Property Tax: $0.00")  # Default label for property tax
label_tax.pack(pady=5)  # Display label with padding

root.geometry("400x200")  # Set window size to 400x200 pixels

# Run the application
root.mainloop()  # Start the Tkinter event loop