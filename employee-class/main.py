#
# Rylee Leavitt
# 2/9/2025
# Employee Class Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.
# I added my own nerdy twist to the employee's :3

# Define the Employee class
class Employee: #defines a new class named Employee

    def __init__(self, name, id_number, department, job_title):
        #initializes the attributes of Employee object when created.

        self.name = name
        #sets the name attribute to the value passed as the name param

        self.id_number = id_number
        #sets the id_number attribute to the value passed as the id_number param

        self.department = department
        #sets the department attribute to the value passed as the department param

        self.job_title = job_title
        #sets the job_title attribute to the value passed as the job_title param

    def display_info(self):
        print(f'Name: {self.name}')             #Prints Name: (the name of the employee)
        print(f'ID Number: {self.id_number}')   #Prints ID Number: (the ID of the employee)
        print(f'Department: {self.department}') #Prints Department: (the Department of the employee)
        print(f'Job Title: {self.job_title}')   #Prints Job Title: (the job title of the employee)
        print()                                 # New line for better readability in between


# Create three Employee objects with the given data
employee1 = Employee('Monika', 2017, 'Doki Doki literature club', 'AI Yandere') 
#Defines employee #1's name, id, department, and title

employee2 = Employee('Ayano Aishi', 2014, 'Yandere Simulator', 'School-girl Yandere') 
#Defines employee #2's name, id, department, and title

employee3 = Employee('Yuno Gasai', 2011, 'Future Diaries', 'Anime Yandere') 
#Defines employee #3's name, id, department, and title

# Display the data for each employee
employee1.display_info() #Displays employee 1 info
employee2.display_info() #Displays employee 2 info
employee3.display_info() #Displays employee 3 info
