import tkinter as tk

# Start the application
root.mainloop()
class AutomotiveGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Joe’s Automotive Services")

        self.services = {
            "Oil change": 30.00,
            "Lube job": 20.00,
            "Radiator flush": 40.00,
            "Transmission flush": 100.00,
            "Inspection": 35.00,
            "Muffler replacement": 200.00,
            "Tire rotation": 20.00
        }

        self.service_vars = {}
        for service in self.services:
            var = tk.IntVar()
            self.service_vars[service] = var
            tk.Checkbutton(root, text=f"{service} - ${self.services[service]:.2f}", variable=var).pack(anchor="w")

        self.total_label = tk.Label(root, text="Total: $0.00", font=("Arial", 12, "bold"))
        self.total_label.pack()

        tk.Button(root, text="Calculate Total", command=self.calculate_total).pack()

    def calculate_total(self):
        total = sum(price for service, price in self.services.items() if self.service_vars[service].get())
        self.total_label.config(text=f"Total: ${total:.2f}")

root = tk.Tk()
app = AutomotiveGUI(root)
root.mainloop()