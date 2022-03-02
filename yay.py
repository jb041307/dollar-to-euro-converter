import tkinter as tk

def dollar_to_euro():
    """
    Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    dollar = ent_temperature.get()
    euro = (9/10) * (float(dollar))
    lbl_result["text"] = f"{round(euro, 2)} €"

# Set-up the window
window = tk.Tk()
window.title("Dollar to Euro")
window.resizable(width=False, height=False)

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="$")

# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=dollar_to_euro
)
lbl_result = tk.Label(master=window, text="€")

# Set-up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()
# just push already