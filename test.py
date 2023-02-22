import requests
import cv2
import numpy as np

url = 'http://127.0.0.1:5000/scan_qr'
my_img = {'image': open('./cap.png', 'rb')}
r = requests.post(url, files=my_img)

# convert server response into JSON format.
print(r.json())
image = cv2.imread("cap.png")

array = []

for data in r.json()["data"]:
    array.append(data['polygon'])

print(array)

pts = np.array(array, np.int32)

color = (255,0,255)
isClosed = True
thickness = 2

image = cv2.polylines(image, pts,
                      isClosed, color, thickness)
 
# Displaying the image
while(1):
     
    cv2.imshow('image', image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
         
cv2.destroyAllWindows()
