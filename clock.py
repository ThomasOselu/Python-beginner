import tkinter as tk
from time import strftime

# Create the root window
root = tk.Tk()
root.title('Digital Clock')

# Function to update the time
def update_time():
    time_string = strftime('%H:%M:%S %p')  # Get the current time
    label.config(text=time_string)         # Update the label's text
    label.after(1000, update_time)         # Call the update function every 1 second

# Create a label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# Start the clock
update_time()

# Run the tkinter main loop
root.mainloop()
