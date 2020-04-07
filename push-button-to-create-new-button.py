from tkinter import Tk, Frame, BOTH
from tkinter.ttk import Style, Button


def make_button(parent, text, position):
    new_button = Button(parent, text=text)
    new_button.place(x=position[0], y=position[1])
    position[1] += 30
    print("id(new_button)", id(new_button))
    # return new_button


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

    my_frame = Frame(root, background="#757")
    my_frame.pack(fill=BOTH, expand=1)

    y = 50

    create_button = Button(my_frame, text="create_button")
    create_button['command'] = lambda arg0=root, arg1="TEXT", arg2=[30,y] : \
                            make_button(arg0, arg1, arg2)
    create_button.place(x=30, y=20)
    root.mainloop()

if __name__ == '__main__':
    main()
