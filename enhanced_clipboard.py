# https://theembeddedlab.com/tutorials/keylogger-python/
# https://stackoverflow.com/questions/1825692/can-python-send-text-to-the-mac-clipboard

from pynput import keyboard
import subprocess
from tkinter import *
import threading

# Set up local vars
currently_pressed = []
current_index = 0
dicti = {}
for i in range(10):
    dicti[i] = ""
clipboard = ""
control_key = False

# Creates the tkinter visuals
def set_up_gui():
	global root
	root = Tk()

	global current

	global button_list

	root.configure(background="#bffff3")
	root.geometry('{}x{}'.format(600, 800))

	button_list = []

	for i in range(10):
		root.grid_rowconfigure(i, weight=1)

	for i in range(10):
		b = Button(root, text=str(i), height=1, highlightbackground='#bffff3')
		b.pack(expand=NO)
		b.grid(row=i,column=1, sticky=N+S+E+W)

		c = Button(root, text=dicti[i], highlightbackground='#bffff3')
		c.pack(expand=YES,fill=BOTH)
		c.grid(row=i,column=2,columnspan=6,sticky=N+S+E+W)

		button_list.append(c)

	current = Button(root, text='CURRENT', height=1, highlightbackground='#bffff3')
	current.pack(expand=NO)
	current.grid(row=0,column=0, sticky=N+S+E+W)
	mainloop()

# Shows the current clipboard slot
def press_button(index):
    current.grid(row=index, column=0)

# Sets the current clipboard slot
def change_text(index, text):
    b = button_list[index]
    b.configure(text=text)
    b.grid(row=index,column=2,columnspan=6,sticky=N+S+E+W)

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

def read_from_clipboard():
    return subprocess.check_output(
        'pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')

def on_press(key):

    global dicti
    global clipboard
    global currently_pressed
    global current_index
    currently_pressed.append(str(key))

    # Sets the user's clipboard according to the current slot
    if 'Key.ctrl' in currently_pressed:
        if isinstance(key, keyboard.KeyCode):
            try:
                current_index = int(key.char)
                write_to_clipboard(dicti[current_index])
                press_button(current_index)
            except:
                pass
    # Saves copied text
    if 'Key.cmd' in currently_pressed and "'c'" in currently_pressed:
        dicti[current_index] = read_from_clipboard()
        change_text(current_index, dicti[current_index])
    elif 'Key.cmd' in currently_pressed and "'x'" in currently_pressed:
        dicti[current_index] = read_from_clipboard()
        change_text(current_index, dicti[current_index])

def on_release(key):
    global currently_pressed
    try:
    	currently_pressed.remove(str(key))
    except:
    	pass
    if str(key) == 'Key.esc':
        print('Exiting...')
        root.quit()
        return False


def set_up_listener():
	with keyboard.Listener(
	    on_press = on_press,
	    on_release = on_release) as listener:
	    listener.join()

def main():
	global t1
	global t2
	t1 = threading.Thread(target=set_up_listener)
	t1.start()
	t2 = set_up_gui()
	return False

if __name__ == '__main__':
    main()



