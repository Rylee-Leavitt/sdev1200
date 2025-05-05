#
# Rylee Leavitt
# 5/4/25
# Population Database Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.

#Import the sqliite3 module
import sqlite3

# main function
def main():
    # menu choice
    choice = 0

    # connect to the database
    conn = sqlite3.connect('cities.db')

    # Get a database cursor
    cur = conn.cursor()

    # Get the user's menu choice
    while choice != 8:
        choice = get_menu_choice()
        execute_choice(choice, cur)

        # close the connection
        conn.close()

# the display_menu function diaplays a menu
def display_menu():
    print('Menu')
    print('-------------------')
    print ('1.) Display a list of cities sorted by population, in ascending order.')
    print ('2.) Display a list of cities sorted by population, in descending order.')
    print ('3.) Display a list of cities sorted by name.')
    print ('4.) Display the total population of all the cities.')
    print ('5.) Display the average population of all the cities.')
    print ('6.) Display the city with the highest population.')
    print ('7.) Display the city with the lowest population.')
    print ('8.) EXIT')

# the get_menu_choice function displays the menu and gets the user's choice
def get_menu_choice ():
        display_menu()
        choice = int(input('Enter your choice (using the corresponding number): '))

        # validate the choice
        while choice < 1 or choice > 8:
            choice = int(input('Enter a valid choice: '))
            
        return choice
        
# preform the action that the user selected
def execute_choice (choice,cur):
        if choice == 1:
            cities_sorted_ascending(cur)

        elif choice == 2:
            cities_sorted_descending(cur)
        
        elif choice == 3:
            cities_sorted_by_name(cur)
        
        elif choice == 4:
            total_population(cur)

        elif choice == 5:
            average_population(cur)
        
        elif choice == 6:
            highest_population(cur)

        elif choice == 7:
            lowest_population(cur)
        
# Display a list of cities sorted by population, in ascending order.
def cities_sorted_ascending(cur):

    # Execute the SELECT statement on the database
    cur.execute(''' SELECT CityName, Population
                FROM Cities
                ORDER By Population''')
    
    # Fetch the results
    results = cur.fetchall()

    # Display the results
    print('\nCitites Sorted By Popluation In Ascending Order')
    print('--------------------------------------------------')
    display_results(results)

# Display a list of cities sorted by population, in descending order.
def cities_sorted_descending(cur):

    # Execute the SELECT statement on the database
    cur.execute(''' SELECT CityName, Population
                FROM Cities
                ORDER By Population DESC''')
    
    # Fetch the results
    results = cur.fetchall()

    # Display the results
    print('\nCitites Sorted By Popluation In Descending Order')
    print('--------------------------------------------------')
    display_results(results)

# Display a list of cities sorted by name.
def cities_sorted_by_name(cur):

    # Execute the SELECT statement on the database
    cur.execute(''' SELECT CityName, Population
                FROM Cities
                ORDER By CityName''')
    
    # Fetch the results
    results = cur.fetchall()

    # Display the results
    print('\nCitites Sorted By Name')
    print('------------------------')
    display_results(results)
    
# Display the total population of all the cities.
def total_population(cur):

    # Execute the SELECT statement on the database
    cur.execute('SELECT SUM(Population) FROM Cities')

    # Fetch the results
    results = cur.fetchone()

    # Display the results
    print(f'\n Total Population: (results[0]:,.0f)\n')

# Display the average population of all the cities.
def average_population(cur):

    # Execute the SELECT statement on the database
    cur.execute('SELECT AVG(Population) FROM Cities')

    # Fetch the results
    results = cur.fetchone()

    # Display the results
    print(f'\n Average Population: (results[0]:,.0f)\n')

# Display the city with the highest population.
def highest_population(cur):

    # get the highest value in the population column
    cur.execute ('SELECT MAX(Population) FROM Cities')

    # Fetch the results
    max_results = cur.fetchone

    # Now, get the entire row that contains that population
    cur.execute ('''SELECT CityName, Population FROM Cities
                 WHERE Population = ?''', (max_results[0],))
    
    # Fetch the ruslts
    results = cur.fetchone()

    # Display the results
    print(f'\n(results[0]) Has The Highest Population: (results[1]:,.0f)\n')

# Display the city with the lowest population.
def lowest_population(cur):

    # Get the lowest value in the population column
    cur.execute ('SELECT MIN(Population) FROM Cities')

    # Fetch the results
    min_results = cur.fetchone

    # Now, get the entire row that contains that population
    cur.execute ('''SELECT CityName, Population FROM Cities
                 WHERE Population = ?''', (min_results[0],))
    
    # Fetch the ruslts
    results = cur.fetchone()

    # Display tyhe results
    print(f'\n(results[0]) Has The Lowest Population: (results[1]:,.0f)\n')

# The display_results function displays the values in
# the results of a SELECT statement. It is assumed that the results contain the 
# CityName and Population columns, in that order.
def display_results(results):
    print(f'("city":20)(Population)')

    for row in results:
        print(f'(row [0]:20)(row [1]:,.0f)')
    print()

# Execute the main function
if __name__ == '__main__':
    main() 
