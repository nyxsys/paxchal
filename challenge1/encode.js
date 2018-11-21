const sha256 = require('js-sha256');
const loki = require('lokijs')
const db = new loki('messages.json')
var messages = db.addCollection('messages')



exports.sha = function(req,res){

    var message = sha256.create();
    message.update(req.body);
    var encode = message.hex();
    messages.insert({'message' : req.body, 'encode' : encode});
    res.send(encode)
}


exports.decode = function(req,res){

    var result = messages.find({'encode' : {'$eq' : req.params.encoded}})
    console.log(result)

    if(result == null || result.length == 0){
        res.status(404).send("404: Message not found.\n");
    }
    else{
        res.send(result[0].message)
    }
}