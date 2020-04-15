from tkinter import Tk, Frame, BOTH
from tkinter.ttk import Style, Button, Label

window_width = 300
window_height = 250


class Command_frame(Frame):
    def __init__(self, parent):
        # Button send
        self.send_button = Button(parent)
        # 'Field'
        self.command = ''

    def send(self):
        self.trim()
        return None # or call smthng like 'serial.send()'

    def trim(self):
        pass


class New_command_frame(Command_frame):
    pass


class Saved_command_frame(Command_frame):
    pass


def set_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_pos_x = 300
    window_pos_y = screen_height - window_height - 30
    window.geometry("%dx%d+%d+%d" % (window_width, window_height, \
                                    window_pos_x, window_pos_y))
    window.title("COMport GUI")


def place_regions_in_window(window, regions):
    # create Frame-objects for regions
    regions['new_command_region'] = Frame(window)
    regions['saved_commands_region'] = Frame(window)
    regions['connection_parameters_region'] = Frame(window)
    # place regions
    regions['new_command_region'].grid(column=1,row=1)
    regions['saved_commands_region'].grid(column=1,row=2)
    regions['connection_parameters_region'].grid(column=1,row=3)


def infill_new_command_region(new_command_region):
    pass


def infill_connection_parameters_region(connection_parameters_region):
    pass


def main():
    root = Tk()
    set_window(root)
    window_regions = {'new_command_region': None,
                     'saved_commands_region': None,
                     'connection_parameters_region': None
                     }
    place_regions_in_window(root, window_regions)
    root.mainloop()


if __name__ == '__main__':
    main()
