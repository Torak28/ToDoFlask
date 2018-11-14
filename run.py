import os, time

print 'Download newest version of db'
os.system('git pull')
print 'Newest db version'

print 'Killing apps running on port 5000'
os.system('sudo kill `sudo lsof -t -i:5000`')
print 'Apps running on port 5000 killed'

print 'Running flask server'
os.system('sudo python3 todo.py &')
print 'Waiting for full configuration and first tests'
time.sleep(30)

print 'Crating a ngrok tunnel'
os.system('sudo ngrok http --region=eu 5000')
