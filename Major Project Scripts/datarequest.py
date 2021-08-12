import requests,os
user, password = 'daicwozuser', 'Tqiy7T7CD9OBTa1VZ5CLjgni'
url = 'https://dcapswoz.ict.usc.edu/wwwdaicwoz/'
os.mkdir('input')
out = 'input/'
for fi in files:
  url +=fi
  resp = requests.get(url, auth=(user, password))
  print('Got file : '+fi)
  open(out+fi, "wb").write(resp.content)