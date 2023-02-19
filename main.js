const express = require('express');
const multer = require('multer');
const qrImage = require('qr-image');
const qrreader = require('qrcode-reader')
const fs = require('fs')

const app = express();
const upload = multer();

app.post('/scan_qr', upload.single('image'), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: 'No image uploaded' });
  }

    const image = qrImage.imageSync(req.file.buffer);
    fs.writeFileSync("image",image);
    

    const qrData = "some data";
    if (!qrData) {
      return res.status(404).json({ error: 'No QR code found' });
    }

    return res.json({ data: qrData });
  });

  app.get("/", (req, res)=>{
    return res.json({ "meeage": "welcome" });
  })


app.listen(3000, () => console.log('Server started on port 3000'));