#
# Rylee Leavitt
# 1/26/2025
# Wi-Fi Diagnostic Tree Programming Project
# SDEV 1200 
#

# Use comments liberally throughout the program.

# function for trouble shooting
def troubleshoot_wifi():
    steps = [
        "Reboot the computer and try to connect.", # asks to Reboot the computer
        "Reboot the router and try to connect.", # asks to Reboot the router
        "Make sure the cables between the router and modem are plugged in firmly.",  # cables plugged?
        "Move the router to a new location.", # move router?
        "Get a new router." # new router?
    ]

    #did that fix the problem?
    
    for step in steps:
        print(step)
        response = input("Did that fix the problem? ").strip().lower()
        if response == "yes":
            break

troubleshoot_wifi()
