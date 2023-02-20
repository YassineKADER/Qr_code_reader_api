import requests
url = 'http://127.0.0.1:5000/scan_qr'
my_img = {'image': open('./qr-code.png', 'rb')}
r = requests.post(url, files=my_img)

# convert server response into JSON format.
print(r.json())