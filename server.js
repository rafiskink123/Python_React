const express = require('express')
const cors = require('cors')
const multer = require('multer')
const upload = multer()

const app = express()
const port = process.env.PORT || 5000 
app.use(express.json())    //all the request comes to it and it transfers to the body of JSON
app.use(cors())       //allow cross origin from client localhost
app.post('/file', upload.single('file'), (req, res) => {console.log('body', req.file.length, req.file)      // creating the endpoint of POST for /file
  res.json({ success: true })    
})

app.listen(port, error => {
  if (error) throw error
  console.log('Server running on port ' + port)
})


// we can run this file by the command < node server.js >
