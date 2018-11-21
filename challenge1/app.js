const express = require('express')
var bodyParser = require('body-parser')
const app = express()

const port = 3000

const encode = require('./encode');


app.use(bodyParser.text());
app.get('/', (req, res) => res.send('Hello World!'))
app.post('/messages', encode.sha);
app.get('/messages/:encoded', encode.decode)
app.listen(port, () => console.log(`listening on port ${port}!`))