#
# Rylee Leavitt
# 5/4/2025
# Phone Book Database Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.

# Import SQLite3 for database operations
import sqlite3

# Create and initialize database
def initialize_db():

    conn = sqlite3.connect('phonebook.db') # Connect to the database (creates if not exists)
    cursor = conn.cursor() 

    # Create a table for storing phonebook entries if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    conn.commit()  # Save changes
    conn.close()  # Close the connection

# Function to add a new entry to the phonebook
def add_entry(name, phone):
    conn = sqlite3.connect('phonebook.db')  # Connect to the database
    cursor = conn.cursor()
    
    # Insert the provided name and phone number into the database
    cursor.execute('INSERT INTO Entries (name, phone) VALUES (?, ?)', (name, phone))
    
    conn.commit()  # Save changes
    conn.close()  # Close the connection
    print(f'Added {name} with phone number {phone}')  # Confirmation message

# Function to lookup a phone number by name
def lookup_phone(name):
    conn = sqlite3.connect('phonebook.db')  # Connect to the database
    cursor = conn.cursor()
    
    # Query the database for the phone number associated with the given name
    cursor.execute('SELECT phone FROM Entries WHERE name = ?', (name,))
    result = cursor.fetchone()  # Fetch the result
    
    conn.close()  # Close the connection
    
    if result:
        print(f'{name}\'s phone number is {result[0]}')  # Display found phone number
    else:
        print(f'No entry found for {name}')  # Message if entry not found

# Function to update an existing phone number
def update_phone(name, new_phone):
    conn = sqlite3.connect('phonebook.db')  # Connect to the database
    cursor = conn.cursor()
    
    # Update the phone number for the given name
    cursor.execute('UPDATE Entries SET phone = ? WHERE name = ?', (new_phone, name))
    
    conn.commit()  # Save changes
    conn.close()  # Close the connection
    print(f'Updated {name}\'s phone number to {new_phone}')  # Confirmation message

# Function to delete an entry by name
def delete_entry(name):
    conn = sqlite3.connect('phonebook.db')  # Connect to the database
    cursor = conn.cursor()
    
    # Delete the entry with the given name
    cursor.execute('DELETE FROM Entries WHERE name = ?', (name,))
    
    conn.commit()  # Save changes
    conn.close()  # Close the connection
    print(f'Deleted entry for {name}')  # Confirmation message

# Main function to interact with the user through a menu
def main():
    initialize_db()  # Ensure the database is initialized before usage

    while True:  # Loop until the user chooses to exit
        print("\nPhonebook CRUD Application")  # Application header
        print("1. Add Entry")  # Option to add a new contact
        print("2. Lookup Phone Number")  # Option to look up a phone number
        print("3. Update Phone Number")  # Option to update a contact
        print("4. Delete Entry")  # Option to delete a contact
        print("5. Exit")  # Option to exit the program
        
        choice = input("Choose an option (using the corresponding option number 1-5): ")  # Get user input

        if choice == '1':  # Add new entry
            name = input("Enter name: ")  # Prompt for name
            phone = input("Enter phone number: ")  # Prompt for phone number
            add_entry(name, phone)  # Call function to add entry
        
        elif choice == '2':  # Lookup phone number
            name = input("Enter name to lookup: ")  # Prompt for name
            lookup_phone(name)  # Call function to look up phone number
        
        elif choice == '3':  # Update phone number
            name = input("Enter name to update: ")  # Prompt for name
            new_phone = input("Enter new phone number: ")  # Prompt for new phone number
            update_phone(name, new_phone)  # Call function to update phone number
        
        elif choice == '4':  # Delete entry
            name = input("Enter name to delete: ")  # Prompt for name
            delete_entry(name)  # Call function to delete entry
        
        elif choice == '5':  # Exit the program
            print("Goodbye!")  # Exit message
            break  # Exit the loop
        
        else:  # Handle invalid input
            print("Invalid choice, please try again.")  # Error message

# Ensure this script runs only when executed directly
if __name__ == "__main__":
    main()
