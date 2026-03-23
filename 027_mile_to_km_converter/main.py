import tkinter as tk


def calculate_km():
    user_miles  = int(label_2.get())
    km = round(user_miles * 1.609344, 2)
    label_3.config(text=km)


window = tk.Tk()
window.title("Converter")
window.config(padx=20, pady=20)
window.minsize(width=300, height=100)

label_1 = tk.Label(text="is equal to")
label_1.grid(column=0, row=1)


label_2 = tk.Entry(width=10)
label_2.grid(column=1, row=0)


label_3 = tk.Label(text="0")
label_3.grid(column=1, row=1)

label_4 = tk.Button(text="Calculate", command=calculate_km)
label_4.grid(column=1, row=2)

label_5 = tk.Label(text="Miles")
label_5.grid(column=2, row=0)

label_6 = tk.Label(text="Km")
label_6.grid(column=2, row=1)

window.mainloop()
