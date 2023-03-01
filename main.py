from tkinter import *
KILOMETERS = 1.60934


def miles_to_km():
    miles = float(miles_input.get())

    d_in_km = miles * KILOMETERS
    km_result_label.config(text=f"{d_in_km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=150)
window.config(padx=20, pady=20)




# input
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1,row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()
