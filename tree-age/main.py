#
# Rylee Leavitt
# 5/4/2025
# Tree Age Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 
import tkinter as tk

# Function to draw growth rings of a tree
def draw_growth_rings(canvas, center_x, center_y, max_radius, num_rings): 

    for i in range(num_rings): #for the rings of the tree

        # Calculate radius for each ring
        radius = (i + 1) * (max_radius // num_rings)
            # max_radius // num_rings divides the maximum radius by the number of rings to determine the width of each ring.
            # (i + 1) ensures that the first ring (innermost) starts at a nonzero radius and each subsequent ring grows outward.
            # i represents the current ring index (starting from 0).
            # max_radius is the maximum radius for the outermost ring.       
            # num_rings is the total number of rings.

        # Draw the ring using an oval shape
        canvas.create_oval(center_x - radius, center_y - radius,
                           center_x + radius, center_y + radius, outline="green", width=4)
        
        # Label the ring with its corresponding year
        canvas.create_text(center_x, center_y - radius + 10, text=str(i+1), fill="black",
                           font=("Arial", 12))

# Create main window
root = tk.Tk()
root.title("Tree Growth Rings")

# Define canvas size
canvas_size = 300
canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
canvas.pack()

# Call function to draw growth rings
draw_growth_rings(canvas, center_x=canvas_size//2, center_y=canvas_size//2, max_radius=120, num_rings=5)
#num_rings = defines the number/range of rings, in this case 5

# Run the Tkinter event loop
root.mainloop()
