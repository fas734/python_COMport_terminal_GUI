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


# start of program
# creates window and graphical elements
root = Tk()
root.title("DarwinTerminal")
root.geometry("600x300")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainFrame = ttk.Frame(root, padding="3 3 3 3")
portFrame = ttk.Frame(root, padding='3 3 3 3')
byte_command_frame = ttk.Frame(mainFrame)
log_frame = ttk.Frame(mainFrame)

# mainFrame elements
send_button = ttk.Button(mainFrame, text="send")
byte_command_entry = ttk.Entry(byte_command_frame, width=50)
byte_command_label = ttk.Label(byte_command_frame, text="byte-like command")
log = Text(log_frame, width=60, height=10)
log_label = ttk.Label(log_frame, text="log")

# portFrame elements
COM_port_number_entry = ttk.Entry(portFrame, width=10)
COM_label = ttk.Label(portFrame, text="COM №")
baudrate_entry = ttk.Entry(portFrame, width=10)
baudrate_label = ttk.Label(portFrame, text="baudrate")
connect_button =  ttk.Button(portFrame, text="Connect")
disconnect_button =  ttk.Button(portFrame, text="Disconnect", command=disconnect)
test_send_button = ttk.Button(portFrame, text="Test", command=test_send)


# positioning all elements
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
portFrame.grid(column=0, row=1, sticky=(N, W, E, S))

send_button.grid(column=1, row=1, sticky=W)
byte_command_frame.grid(column=2, row=1, sticky=(W, E))
byte_command_label.grid(column=1, row=1, sticky=(W, E))
byte_command_entry.grid(column=1, row=2, sticky=(W, E))
log_frame.grid(column=2, row=2, columnspan=2, sticky=(W, E))
log_label.grid(column=1, row=1, sticky=(W, E))
log.grid(column=1, row=2, sticky=(W, E))

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
send_button['command'] = lambda arg1=byte_command_string : send(arg1)

COM_port = serial.Serial()
for child in mainFrame.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', lambda event, arg1=byte_command_string : send(arg1))

root.mainloop()
