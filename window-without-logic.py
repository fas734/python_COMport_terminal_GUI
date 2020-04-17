from tkinter import Tk, Frame, BOTH
from tkinter.ttk import Style, Button, Label, Entry

window_width = 300
window_height = 250


class Command_frame(Frame):

    def __init__(self, parent, **kwargs):
        super(Command_frame, self).__init__(parent, **kwargs)
        # Button send
        self.send_button = Button(parent, text="SEND")
        # 'Field'
        self.command = ''

    def send(self):
        self.trim()
        return None # or call smthng like 'serial.send()'

    def trim(self):
        pass


class New_command_frame(Command_frame):

    def __init__(self, parent, **kwargs):
        super(New_command_frame, self).__init__(parent, **kwargs)
        self.save_button = Button(parent, text="SAVE")
        self.command_entry = Entry(parent, width=15)

        self.save_button.grid(column=1, row=1)
        self.command_entry.grid(column=2, row=1)
        self.send_button.grid(column=3, row=1)

    def save(self):
        pass


class Saved_command_frame(Command_frame):

    def __init__(self, parent, **kwargs):
        super(Saved_command_frame, self).__init__(parent, **kwargs)
        self.del_button = Button(parent, text="DEL")
        self.command_name = "command_name"
        self.command_name_label = Label(parent, text=self.command_name)

        self.del_button.grid(column=1, row=1)
        self.command_name_label.grid(column=2, row=1)
        self.send_button.grid(column=3, row=1)

    def delete(self):
        pass

    def change_name(self):
        pass


class Connection_parameters_frame(Frame):

    def __init__(self, parent, **kwargs):
        super(Connection_parameters_frame, self).__init__(parent, **kwargs)
        self.connect_button = Button(parent, text="Connect")
        self.disconnect_button = Button(parent, text="Disconnect")
        self.port_number = ""
        self.port_number_label = Label(parent, text="Port number:")
        self.port_number_entry = Entry(parent, width=10)
        self.baudrate = ""
        self.baudrate_label = Label(parent, text="Baudrate:")
        self.baudrate_entry = Entry(parent, width=10)

        self.connect_button.grid(column=1, row=1)
        self.disconnect_button.grid(column=1, row=2)
        self.port_number_label.grid(column=2, row=1)
        self.port_number_entry.grid(column=2, row=2)
        self.baudrate_label.grid(column=3, row=1)
        self.baudrate_entry.grid(column=3, row=2)

    def connect(self):
        pass

    def disconnect(self):
        pass

    def read_parameters(self):
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
    new_command_frame = New_command_frame(new_command_region)
    new_command_frame.grid(column=1, row=1)


def show_saved_commands(parent): # JUST TO SHOW! Will be deleted in next commit
    saved_command_frame = Saved_command_frame(parent)
    saved_command_frame.grid(column=1, row=1)


def infill_connection_parameters_region(connection_parameters_region):
    connection_parameters_frame \
                = Connection_parameters_frame(connection_parameters_region)
    connection_parameters_frame.grid(column=1, row=1)


def main():
    root = Tk()
    set_window(root)
    window_regions = {'new_command_region': None,
                     'saved_commands_region': None,
                     'connection_parameters_region': None
                     }
    place_regions_in_window(root, window_regions)
    infill_new_command_region(window_regions['new_command_region'])
    show_saved_commands(window_regions['saved_commands_region']) # just to show
    infill_connection_parameters_region(window_regions\
                                        ['connection_parameters_region'])
    root.mainloop()


if __name__ == '__main__':
    main()
