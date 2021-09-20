from tkinter import *
from tkinter.ttk import *
from transposer import *
#from transpose_functions import increment_key, key_difference, key_nature


def key_handle(event):
    print("edit-detected")

    current_key.config(state="enabled")
    desired_key.config(state="enabled")

    raw_text = text_box.get("1.0", "end")
    key = determine_key(raw_text)
    current_key.delete("0", "end")
    current_key.insert("0", key)

    desired_key.delete("0", "end")
    desired_key.insert("0", key)

    current_key.config(state="disabled")
    desired_key.config(state="disabled")

def plus_button_handle(event):

    desired_key.config(state="enabled")

    c_key = desired_key.get()
    new_key = increment_key(c_key, "UP")

    desired_key.delete("0", "end")
    desired_key.insert("0", new_key)

    desired_key.config(state="disabled")


def minus_button_handle(event):
    desired_key.config(state="enabled")

    c_key = desired_key.get()
    new_key = increment_key(c_key, "DOWN")

    desired_key.delete("0", "end")
    desired_key.insert("0", new_key)

    desired_key.config(state="disabled")


def transpose_handle_click(event):
    raw_text = text_box.get("1.0", "end")

    d_key = desired_key.get()
    c_key = current_key.get()

    num_steps = key_difference(c_key, d_key)

    if key_nature(d_key):
        sharp = True
    else:
        sharp = False
    transposed_text = transpose(raw_text, num_steps, sharp)

    text_box.delete("1.0", "end")
    text_box.insert("1.0", transposed_text)

    key_handle("<KeyRelease>")


master = Tk()
master.title("Song Transposer")

key_label = Label(text="Current Key:")
key_label.grid(row=1, column=0)

desired_key_label = Label(text="Desired Key:")
desired_key_label.grid(row=2, column=0)

current_key = Entry(width=5, state="disabled")
current_key.grid(row=1, column=1)

desired_key = Entry(width=5, state="disabled")
desired_key.grid(row=2, column=1)

transpose_button = Button(text="Transpose")
transpose_button.bind("<Button-1>", transpose_handle_click)
transpose_button.grid(row=0, columnspan=4)

plus_button = Button(text="+")
plus_button.bind("<Button-1>", plus_button_handle)
plus_button.grid(row=2,column=2)

minus_button = Button(text="-")
minus_button.bind("<Button-1>", minus_button_handle)
minus_button.grid(row=2,column=3)

#scale = Scale(master,orient="horizontal", from_="-11", to="11",sliderlength=30)
#scale.pack()

text_box = Text(width=100, height=50)
text_box.insert(5.15, "Insert Song Here")

text_box.bind("<KeyRelease>", key_handle)
text_box.grid(row=3, columnspan=4)

master.update()
mainloop()