const axios = require("axios");
const fs = require('fs');
const img = fs.readFileSync("../qr-code.png")

axios.post("http://127.0.0.1:3000/scan_qr",img,{
    headers:{
        'content-type': 'multipart/form-data; boundary="hello"'
    }
}).then(()=>{
    console.log("success !!");
}).catch((error)=>{
    console.log(error)
    console.log("alert!!");
})