from tkinter import Tk, Frame, BOTH
from tkinter.ttk import Style, Button


def delete_widget(widget0, widget1):
    widget0.destroy()
    widget1.destroy()
    # or just delete a parent widget


# example code
# NOTE: run with -i option
def main():
    root = Tk()
    root.geometry("250x250+250+500")

    my_frame = Frame(root, background="#535")
    my_frame.pack(fill=BOTH, expand=1)
    another_frame = Frame(root, background="#434")
    another_frame.pack(fill=BOTH, expand=1)

    new_button = Button(my_frame, text="Button")
    new_button.place(x=10, y=10)
    delete_button = Button(another_frame, text="<-delete")
    delete_button.place(x=100, y=10)
    delete_button["command"] = lambda : delete_widget(my_frame, another_frame)

    root.mainloop()

if __name__ == '__main__':
    main()
