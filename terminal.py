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
        self.command_var = StringVar()
        self.command_entry = Entry(self, width=15, \
                                   textvariable=self.command_var)

    def send(self):
        self.trim()
        #TODO# send if opened else warn
        COMport.write(bytes.fromhex(self.command))
        print("Sended:", bytes.fromhex(self.command))

    def trim(self):
        # don't trim if it was cleaned already
        if self.command == self.command_var.get():
            return
        self.command = ''
        tmp = self.command_var.get()
        # removes all inappropriate symbols and spaces
        for l in tmp:
            if not (l in '0123456789abcdefABCDEF'):
                tmp = tmp.replace(l,'')
        # removes last odd symbol if present
        if len(tmp)%2 == 1:
            tmp = tmp[:len(tmp)-1]
        # split command with spaces for convenience
        for i in range(0,len(tmp),2):
            self.command = self.command + tmp[i] + tmp[i+1] + ' '
        # removes last space
        self.command = self.command[:-1]
        self.command_var.set(self.command)


class New_command_frame(Command_frame):

    def __init__(self, parent, **kwargs):
        super(New_command_frame, self).__init__(parent, **kwargs)
        self.save_button = Button(self, text="SAVE")

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
        saved = Saved_command_frame(window_regions['saved_commands_region'])
        saved.command_var.set(self.command_var.get())


class Saved_command_frame(Command_frame):

    def __init__(self, parent, **kwargs):
        super(Saved_command_frame, self).__init__(parent, **kwargs)
        self.del_button = Button(self, text="DEL")
        self.command_name = "command_name"
        self.command_name_label = Label(self, text=self.command_name)

        self.del_button.grid(column=0, row=0, rowspan=2)
        self.command_entry.grid(column=1, row=0)
        self.command_entry.grid_remove()    # hide that Entry
        self.command_name_label.grid(column=1, row=1)
        self.send_button.grid(column=2, row=0, rowspan=2)
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
        #TODO# open if not opened
        COMport.open()
        print("Connected to", COMport.port, 'at', COMport.baudrate, 'bauds.')

    def disconnect(self):
        #TODO# close if opened
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
    show_example_of_saved_command(regions['saved_commands_region'])
    infill_connection_parameters_region(regions\
                                        ['connection_parameters_region'])


def infill_new_command_region(new_command_region):
    new_command_frame = New_command_frame(new_command_region)


def show_example_of_saved_command(saved_commands_region): # just to show
    saved_command_frame = Saved_command_frame(saved_commands_region)
    saved_command_frame.command_var.set('48 65 6c 6c 6f 21 20 3a 29 0a')
    saved_command_frame.command_name_label['text'] = "Hello! :)\n[" \
                                + saved_command_frame.command_var.get() + ']'


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
