#
# Rylee Leavitt
# 4/28/25
# Joe's Automotive Programming Project
# SDEV 1200

# Use comments liberally throughout the program.  
# The code below was auto-generated. 
# Delete/adjust unnecessary code.

import tkinter
import tkinter.messagebox

class AutoGUI:
    def __init__(self):
        #create main window
        self.main_window = tkinter.tk()

        #create frames
        self.top_frame = tkinter(self.main_window)
        self.bottom_frame = tkinter (self.main_window)

        #create variables to use with the check buttons
        self.cb_oil_var = tkinter.IntVar()
        self.cb_lube_var = tkinter.IntVar()
        self.cb_radiator_var = tkinter.IntVar()
        self.cb_trans_var = tkinter.IntVar()
        self.cb_inspection_var = tkinter.IntVar()
        self.cb_muffler_var = tkinter.IntVar()
        self.cb_tire_var = tkinter.IntVar()

        #set the variables to 0
        self.cb_oil_var.set (0)
        self.cb_lube_var.set (0)
        self.cb_radiator_var.set (0)
        self.cb_trans_var.set (0)
        self.cb_inspection_var.set (0)
        self.cb_muffler_var.set (0)
        self.cb_tire_var.set (0)

        #create the checkbuttons in top frame
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                    text= 'Oil Change - $30.00',
                    variable= self.cb_oil_var)
        
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                    text= 'Lube Job - $20.00',
                    variable= self.cb_lube_var)
        
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                    text= 'Radiator Flush - $40.00',
                    variable= self.cb_radiator_var)
        
        self.cb4 = tkinter.Checkbutton(self.top_frame,
                    text= 'Transmission Flush - $100.00',
                    variable= self.cb_trans_var)
        
        self.cb5 = tkinter.Checkbutton(self.top_frame,
                    text= 'Inspection - $35.00',
                    variable= self.cb_inspection_var)
        
        self.cb6 = tkinter.Checkbutton(self.top_frame,
                    text= 'Muffler replacement - $200.00',
                    variable= self.cb_muffler_var)
        
        self.cb7 = tkinter.Checkbutton(self.top_frame,
                    text= 'Tire rotation - $20.00',
                    variable= self.cb_tire_var)
        
        #packing the check buttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        #create two buttons in the bottom frame
        self.display_button = tkinter.Button(self.bottom_frame,
                            text= 'Display Charges',
                            command= self.calculate)
        
        self.quit_button = tkinter.Button(self.bottom_frame,
                            text= 'Quit',
                            command= self.main_window.destroy)

        #pack the widgets in the bottom frame
        self.display_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        #pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        #enter the tkinter main loop
        tkinter.mainloop()

    #define the show infor function
    def calculate(self):
        self.total = 0.0

        #determine the total charges based on the buttons pressed
        if self.cb_oil_var.get() == 1:
            self.total += 30.0

        if self.cb_lube_var.get() == 1:
            self.total += 20.0
        
        if self.cb_radiator_var.get() == 1:
            self.total += 40.0
        
        if self.cb_trans_var.get() == 1:
            self.total += 100.0

        if self.cb_inspection_var.get() == 1:
            self.total += 35.0
        
        if self.cb_muffler_var.get() == 1:
            self.total += 200.0
        
        if self.cb_tire_var.get() == 1:
            self.total += 20.0

        #Display message box
        tkinter.messagebox.showinfo('Total Charges',
                        f'Your Total Charges - ${self.total:,.2f}')

#create an instace of auto GUI
if __name__ == '__main__':
    auto = AutoGUI()