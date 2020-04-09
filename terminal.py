import serial
from tkinter import *
from tkinter import ttk
import time


# send byte-like string, takes StringVar()
def send(command):
    command_string = command.get()
    log.insert(1.0, command_string+'\n')
    COM_port.write(bytearray.fromhex(command_string))


def connect(port, baudrate, *args):
    port = port.get()
    baudrate = baudrate.get()

    if port == '':
    	port = '11'
    port = "COM" + port
    if baudrate == 0:
        baudrate = 57600

    print ('... connection to', port, "with", baudrate, "bods", '...')

    COM_port.port = port
    COM_port.baudrate = 56000
    COM_port.open()
    print ('Connected to', port)


def disconnect(*args):
    COM_port.close()

    
# any send commands to make sure it works
def test_send(*args):
    log.insert(1.0, 'test\n')
    COM_port.write(bytearray.fromhex('FF FF FD 00 FE 0A 00 83 1E 00 02 00 02 58 02 A0 32'))
    time.sleep(1)
    COM_port.write(bytearray.fromhex('FF FF FD 00 FE 0A 00 83 1E 00 02 00 02 00 02 A6 E2'))


def make_tack(parent):
    tack_inframe = ttk.Frame(parent)
    tack_inframe.grid(column=1, sticky=(W, E))
    tack_del_button = ttk.Button(tack_inframe, text="DEL")
    tack_del_button.grid(column=1, row=1, sticky=(W, E))
    tack_del_button['command'] = lambda widget=tack_inframe : delete_widget(widget)
    tack_label = ttk.Label(tack_inframe, text="tack_label")
    tack_label.grid(column=2, row=1, sticky=(W, E))
    tack_send_button = ttk.Button(tack_inframe, text="SEND")
    tack_send_button.grid(column=3, row=1, sticky=(W, E))
    # print("id(tack_inframe)", id(tack_inframe))
    # return tack_inframe


def delete_widget(widget):
    widget.destroy()


# start of program
# creates window and graphical elements
root = Tk()
root.title("DarwinTerminal")
root.geometry("600x300")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame = ttk.Frame(root, padding="3 3 3 3")
byte_command_frame = ttk.Frame(main_frame)
tacks_frame = ttk.Frame(main_frame)
log_frame = ttk.Frame(main_frame)
portFrame = ttk.Frame(root, padding='3 3 3 3')

# main_frame elements
byte_command_add_button = ttk.Button(byte_command_frame, text="ADD")
byte_command_frame_inframe = ttk.Frame(byte_command_frame)
byte_command_label = ttk.Label(byte_command_frame_inframe, \
                                text="byte-like command")
byte_command_entry = ttk.Entry(byte_command_frame_inframe, width=50)
byte_command_send_button = ttk.Button(byte_command_frame, text="send")

log_label = ttk.Label(log_frame, text="log")
log = Text(log_frame, height=4)


# portFrame elements
COM_port_number_entry = ttk.Entry(portFrame, width=10)
COM_label = ttk.Label(portFrame, text="COM №")
baudrate_entry = ttk.Entry(portFrame, width=10)
baudrate_label = ttk.Label(portFrame, text="baudrate")
connect_button =  ttk.Button(portFrame, text="Connect")
disconnect_button =  ttk.Button(portFrame, text="Disconnect", command=disconnect)
test_send_button = ttk.Button(portFrame, text="Test", command=test_send)


# positioning all elements
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

byte_command_frame.grid(column=1, row=1, sticky=(N, W, E))
byte_command_add_button.grid(column=1, row=1, sticky=(W,E))
byte_command_frame_inframe.grid(column=2, row=1, sticky=(W,E))
byte_command_label.grid(column=1, row=1, sticky=(W, E))
byte_command_entry.grid(column=1, row=2, sticky=(W, E))
byte_command_send_button.grid(column=3, row=1, sticky=W)

tacks_frame.grid(column=1, row=2, sticky=(N,W,E,S))
tacks_label = ttk.Label(tacks_frame, text="tacks_label")
tacks_label.grid(column=1, row=0, sticky=(W,E))

log_frame.grid(column=1, row=3, columnspan=2, sticky=(W, E, S))
log_label.grid(column=1, row=1, sticky=(W, E))
log.grid(column=1, row=2, sticky=(W, E))

portFrame.grid(column=0, row=1, sticky=(N, W, E, S))

connect_button.grid(column=1, row=1, sticky=W)
disconnect_button.grid(column=1, row=2, sticky=W)
COM_label.grid(column=2, row=1)
COM_port_number_entry.grid(column=2, row=2, sticky=W)
baudrate_label.grid(column=3, row=1)
baudrate_entry.grid(column=3, row=2)
test_send_button.grid(column=10, row=2, sticky=W)


# bind GUI with logics
COM_port_number = StringVar()       # number only, like "12" not "COM12"
byte_command_string = StringVar()
baudrate_string = StringVar()

COM_port_number_entry["textvariable"] = COM_port_number
byte_command_entry["textvariable"] = byte_command_string
baudrate_entry["textvariable"] = baudrate_string
connect_button['command'] = lambda arg0=COM_port_number, arg1=baudrate_string : connect(arg0, arg1)
byte_command_send_button['command'] = lambda arg1=byte_command_string : send(arg1)
byte_command_add_button['command'] = lambda parent=tacks_frame : make_tack(parent)

COM_port = serial.Serial()
for child in main_frame.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', lambda event, arg1=byte_command_string : send(arg1))

root.mainloop()
