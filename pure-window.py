from tkinter import *   # maybe Tk is enough?
from tkinter import ttk


def main():
    window_width = 300
    window_height = 250
    root = Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_pos_x = 300
    window_pos_y = screen_height - window_height - 30
    root.geometry("%dx%d+%d+%d" % (window_width, window_height, \
                                    window_pos_x, window_pos_y))
    root.title("Buttons")

    root.mainloop()  


if __name__ == '__main__':
    main()
