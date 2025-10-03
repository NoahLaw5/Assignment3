import tkinter as tk

#Creates the window
window = tk.Tk()
window.title("Miles per Gallon to Kilometers per liter Converter")
window.geometry("400x400")


def convert(event= None):

    #Converts input of MPG to kml
    try:
        mpg = float (mpg_entry.get())

        kml = mpg * 0.425143707

        result_label.config(text=f"{kml:.2f}")

    #keeps the program from crashing despite input
    except:

        result_label.config(text="")

#Creates label for input
mpg_label = tk.Label(window, text = "Enter Miles per Gallon: ")
mpg_label.pack(pady=5)

#Creates entry box
mpg_entry = tk.Entry(window)
mpg_entry.pack(pady=5)
mpg_entry.bind("<KeyRelease>", convert)

#Creates result label
result_label = tk.Label(window, text="", font=("Arial", 12), fg="green")
result_label.pack(pady=10)

#Runs program
window.mainloop()