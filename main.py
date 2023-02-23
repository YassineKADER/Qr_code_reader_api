from flask import Flask, jsonify, request
from pyzbar.pyzbar import decode
from PIL import Image

app = Flask(__name__)

def read_qr_code(img):
    try:
        value = decode(img)
        data = []
        for barcode in value:
            data.append({'data':barcode.data.decode("utf-8"), 'type':barcode.type,'polygon':barcode.polygon})
        return data
    except:
        return
    
@app.route('/scan_qr', methods=['POST','Get'])
def scan_qr():
    print(request)
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    img_file = request.files['image']
    img = Image.open(img_file.stream)
    results = read_qr_code(img)
    if results == None:
        return jsonify({'error': results}), 404
    qr_data = results
    return jsonify({'data': qr_data}), 200

if __name__ == '__main__':
    app.run(debug=True)