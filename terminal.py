from tkinter import Tk, Frame, StringVar, IntVar
from tkinter.ttk import Button, Label, Entry
from tkinter.constants import *
import serial

window_width = 380
window_height = 250

COMport = serial.Serial(timeout=0.5)


class Command_frame(Frame):

    def __init__(self, parent, **kwargs):
        super(Command_frame, self).__init__(parent, **kwargs)
        # Button send
        self.send_button = Button(self, text="SEND", command=self.send)
        # 'Field'
        self.command = ''

    def send(self):
        self.trim()
        # send if opened else warn
        COMport.write(bytes.fromhex(self.command))
        print("Sended:", bytes.fromhex(self.command))

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
        self.connect_button = Button(self, text="Connect", \
                                     command=self.connect)
        self.disconnect_button = Button(self, text="Disconnect", \
                                        command=self.disconnect)
        self.port_number = "/dev/ttyUSB0"
        self.port_number_var = StringVar(value=self.port_number)
        self.port_number_label = Label(self, text="Port number:")
        self.port_number_entry = Entry(self, width=12, \
                                       textvariable=self.port_number_var)
        self.baudrate = 115200
        self.baudrate_var = IntVar(value=self.baudrate)
        self.baudrate_label = Label(self, text="Baudrate:")
        self.baudrate_entry = Entry(self, width=10, \
                                    textvariable=self.baudrate_var)

        self.connect_button.grid(column=0, row=0)
        self.disconnect_button.grid(column=0, row=1)
        self.port_number_label.grid(column=1, row=0)
        self.port_number_entry.grid(column=1, row=1)
        self.baudrate_label.grid(column=2, row=0)
        self.baudrate_entry.grid(column=2, row=1)
        self.grid()

    def connect(self):
        self.read_parameters()
        # open if not opened
        COMport.open()
        print("Connected to", COMport.port, 'at', COMport.baudrate, 'bauds.')

    def disconnect(self):
        # close if opened
        COMport.close()
        print("Disconnected.")

    def read_parameters(self):
        self.port_number = self.port_number_var.get().strip()
        # makes port_number_entry show current value of port_number
        self.port_number_var.set(self.port_number)

        self.baudrate = self.baudrate_var.get()
        # makes baudrate_entry show current value of baudrate
        self.baudrate_var.set(self.baudrate)

        COMport.port = self.port_number
        COMport.baudrate = self.baudrate


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
    # infill regions
    infill_new_command_region(regions['new_command_region'])
    show_saved_commands(regions['saved_commands_region']) # just to show
    infill_connection_parameters_region(regions\
                                        ['connection_parameters_region'])


def infill_new_command_region(new_command_region):
    new_command_frame = New_command_frame(new_command_region)


def show_saved_commands(parent): # JUST TO SHOW! Will be deleted in next commit
    saved_command_frame = Saved_command_frame(parent)
    saved_command_frame.command = '48 65 6c 6c 6f 21 20 3a 29 0a' # Hello! :)\n
    saved_command_frame.command_name_label['text'] = "For show purpose\n[" \
                                            + saved_command_frame.command + ']'


def infill_connection_parameters_region(connection_parameters_region):
    connection_parameters_frame \
                = Connection_parameters_frame(connection_parameters_region)


def main():
    root = Tk()
    set_window(root)
    global window_regions
    window_regions = {'new_command_region': None,
                     'saved_commands_region': None,
                     'connection_parameters_region': None }
    place_regions_in_window(root, window_regions)

    root.mainloop()


if __name__ == '__main__':
    main()
