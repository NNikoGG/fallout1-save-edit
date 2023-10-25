import tkinter as tk
from tkinter import filedialog

# Function to convert a decimal value to hexadecimal
def decimal_to_hex(decimal_value):
    return hex(decimal_value).lstrip("0x").zfill(2)

# Function to apply changes to the save file
def apply_changes():
    file_path = file_path_entry.get()
    new_hp = int(new_hp_entry.get())  # Get the user's desired HP as an integer
    new_hp_hex = decimal_to_hex(new_hp)  # Convert to hexadecimal

    try:
        with open(file_path, "r+b") as file:
            # Navigate to the offset and column to change the HP value
            file.seek(0x895A)
            file.write(bytearray.fromhex(new_hp_hex))
            status_label.config(text="HP Updated Successfully")
    except FileNotFoundError:
        status_label.config(text="File not found")
    except Exception as e:
        status_label.config(text=f"An error occurred: {str(e)}")

# Create the main application window
app = tk.Tk()
app.title("Fallout 1 Save Editor")

# Create and configure GUI elements
file_path_label = tk.Label(app, text="Select SAVE.DAT File:")
file_path_entry = tk.Entry(app)
file_browse_button = tk.Button(app, text="Browse", command=lambda: file_path_entry.insert(0, filedialog.askopenfilename(title="Select SAVE.DAT File")))
new_hp_label = tk.Label(app, text="Enter New HP (Decimal):")
new_hp_entry = tk.Entry(app)
apply_button = tk.Button(app, text="Apply Changes", command=apply_changes)
status_label = tk.Label(app, text="")

# Position GUI elements in the window
file_path_label.pack()
file_path_entry.pack()
file_browse_button.pack()
new_hp_label.pack()
new_hp_entry.pack()
apply_button.pack()
status_label.pack()

# Start the Tkinter main loop
app.mainloop()
