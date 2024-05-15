
import tkinter as tk
from tkinter import *
import math
from number_entry import IntEntry

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#eb1c1c"
# "#e7305b"
GREEN = "#4CBB17"
ORANGE = "#FFB025"
YELLOW = "#f7f5dd"
BLUE = "#7EC8E3"
NAVY_BLUE = "#000C66"
FONT_NAME = "Counter-Strike"


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Calculate Area of Circle")
    frm_main.pack(padx=165, pady=140, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

    # area = calculate_circle_area(ent_radius=1)
    # area = populate_main_window(ent_radius)
    # radius = populate_main_window(ent_radius)
    # print(radius)


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """

    lbl_radius = Label(frm_main, text="Enter the radius:")

    # Create an integer entry box where the user will enter the radius.
    ent_radius = IntEntry(frm_main, width=4)

    lbl_area_text = Label(frm_main, text="Area:")
    lbl_area_value = Label(frm_main, text="")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(row=0, column=0, padx=3, pady=3)
    ent_radius.grid(row=0, column=1, padx=3, pady=3)
    # lbl_area.grid(row=0, column=2, padx=0, pady=3)

    lbl_area_text.grid(row=1, column=0, padx=3, pady=3)
    lbl_area_value.grid(row=1, column=1, padx=3, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")


# This function will be called each time the user releases a key.

    def calculate_area_circle(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            radius = ent_radius.get()

            area = math.pi * radius ** 2

            # lbl_area.config(text="Area:")
            lbl_area_value.config(text=f"{area:.0f}")

        except ValueError:

            lbl_area_value.config(text="")

    # This function will be called each time
    # the user presses the "Clear" button.

    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_radius.clear()
        lbl_area_value.config(text="")
        ent_radius.focus()

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_radius.bind("<KeyRelease>", calculate_area_circle)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_radius.focus()


# def calculate_circle_area(ent_radius):
#     area = math.pi * ent_radius ** 2

#     return area
if __name__ == "__main__":
    main()


# ---------------------------- UI SETUP ------------------------------- #
# window = Tk()
# window.title("Pomodoro")
# window.config(padx=100, pady=50, bg=YELLOW)

# # Timer Label
# timer_label = Label(fg=BLUE, bg=YELLOW, text="Timer",
#                     font=(FONT_NAME, 40, "bold"))
# timer_label.grid(column=1, row=0)

# # Checkmark Label
# checkmarks = Label(fg=RED, bg=YELLOW)
# checkmarks.grid(column=1, row=5)

# # Canvas
# canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# # tomato_img = PhotoImage(file="tomato.png")
# # canvas.create_image(100, 112, image=tomato_img)
# timer_text = canvas.create_text(
#     100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.grid(column=1, row=2)

# window.mainloop
