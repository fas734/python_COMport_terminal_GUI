from tkinter import Tk, Frame
from tkinter.constants import *
from tkinter.ttk import Style, Button, Label, Entry

window_width = 360
window_height = 250


class Command_frame(Frame):

    def __init__(self, parent, **kwargs):
        super(Command_frame, self).__init__(parent, **kwargs)
        # Button send
        self.send_button = Button(self, text="SEND")
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
        self.save_button = Button(self, text="SAVE")
        self.command_entry = Entry(self, width=15)

        self.rowconfigure(0, pad=5)
        self.columnconfigure(0, weight=1, pad=5)
        self.columnconfigure(1, weight=1, pad=5)
        self.columnconfigure(2, weight=1, pad=5)

        self.save_button.grid(column=0, row=0, sticky=W)
        self.command_entry.grid(column=1, row=0, sticky=EW)
        self.send_button.grid(column=2, row=0, sticky=E)
        self.grid()

        self.save_button['command'] = lambda : self.save()

    def save(self):
        Saved_command_frame(window_regions['saved_commands_region'])


class Saved_command_frame(Command_frame):

    def __init__(self, parent, **kwargs):
        super(Saved_command_frame, self).__init__(parent, **kwargs)
        self.del_button = Button(self, text="DEL")
        self.command_name = "command_name"
        self.command_name_label = Label(self, text=self.command_name)

        self.del_button.grid(column=1, row=0)
        self.command_name_label.grid(column=2, row=0)
        self.send_button.grid(column=3, row=0)
        self.grid()

        self.del_button['command'] = lambda : self.delete()

    def delete(self):
        self.destroy()

    def change_name(self):
        pass


class Connection_parameters_frame(Frame):

    def __init__(self, parent, **kwargs):
        super(Connection_parameters_frame, self).__init__(parent, **kwargs)
        self.connect_button = Button(self, text="Connect")
        self.disconnect_button = Button(self, text="Disconnect")
        self.port_number = ""
        self.port_number_label = Label(self, text="Port number:")
        self.port_number_entry = Entry(self, width=10)
        self.baudrate = ""
        self.baudrate_label = Label(self, text="Baudrate:")
        self.baudrate_entry = Entry(self, width=10)

        self.connect_button.grid(column=0, row=0)
        self.disconnect_button.grid(column=0, row=1)
        self.port_number_label.grid(column=1, row=0)
        self.port_number_entry.grid(column=1, row=1)
        self.baudrate_label.grid(column=2, row=0)
        self.baudrate_entry.grid(column=2, row=1)

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
    window_pos_y = screen_height - window_height - 28
    window.geometry("%dx%d+%d+%d" % (window_width, window_height, \
                                    window_pos_x, window_pos_y))
    window.title("COMport GUI")
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)


def place_regions_in_window(window, regions):
    # create Frame-objects for regions
    regions['new_command_region'] = Frame(window)
    regions['saved_commands_region'] = Frame(window)
    regions['connection_parameters_region'] = Frame(window)
    # place regions
    regions['new_command_region'].grid(column=0, row=0, sticky=N)
    regions['saved_commands_region'].grid(column=0, row=1, sticky=NS)
    regions['connection_parameters_region'].grid(column=0, row=2, sticky=S)


def infill_new_command_region(new_command_region):
    new_command_frame = New_command_frame(new_command_region)


def show_saved_commands(parent): # JUST TO SHOW! Will be deleted in next commit
    saved_command_frame = Saved_command_frame(parent)
    saved_command_frame.command_name_label['text'] = "For show purpose only"


def infill_connection_parameters_region(connection_parameters_region):
    connection_parameters_frame \
                = Connection_parameters_frame(connection_parameters_region)
    connection_parameters_frame.grid(column=0, row=0)


def main():
    root = Tk()
    set_window(root)
    global window_regions
    window_regions = {'new_command_region': None,
                     'saved_commands_region': None,
                     'connection_parameters_region': None }
    place_regions_in_window(root, window_regions)
    infill_new_command_region(window_regions['new_command_region'])
    show_saved_commands(window_regions['saved_commands_region']) # just to show
    infill_connection_parameters_region(window_regions\
                                        ['connection_parameters_region'])
    root.mainloop()


if __name__ == '__main__':
    main()
