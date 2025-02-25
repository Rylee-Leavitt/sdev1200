#
# Rylee Leavitt
# 2/24/25
# Employee And ProductionWorker Classes Programming Project
# SDEV 1200
#

# main.py
from production_Workers import Production_Worker

def main():
    # Get employee information from user
    name = input("Enter the employee's name: ")
    number = input("Enter the employee's number: ")
    shift = int(input("Enter the shift number (1 for day, 2 for night): "))
    pay_rate = float(input("Enter the hourly pay rate: "))

    # Create an instance of ProductionWorker
    worker = Production_Worker(name, number, shift, pay_rate)

    # Display the employee information
    print("\nEmployee Information:")
    print("Name:", worker.get_name())
    print("Number:", worker.get_number())
    print("Shift:", "Day" if worker.get_shift() == 1 else "Night")
    print("Hourly Pay Rate: $", format(worker.get_pay_rate(), ".2f"), sep="")

if __name__ == "__main__":
    main()
