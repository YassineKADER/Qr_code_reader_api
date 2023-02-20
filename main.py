from flask import Flask, jsonify, request
from PIL import Image
import cv2
app = Flask(__name__)

def read_qr_code(filename):
    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        return value
    except:
        return

print(read_qr_code("./qr-code.png"))

"""
@app.route('/scan_qr', methods=['POST'])
def scan_qr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    img_file = request.files['image'].read()
    img = Image.open(io.BytesIO(img_file))
    scanner = zbar.Scanner()
    results = scanner.scan(img.convert('L'))

    if not results:
        return jsonify({'error': 'No QR code found'}), 404

    qr_data = results[0].data.decode('utf-8')
    return jsonify({'data': qr_data}), 200

if __name__ == '__main__':
    app.run()
"""