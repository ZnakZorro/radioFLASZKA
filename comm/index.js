var app  = require("/usr/local/lib/node_modules/express");
var http = require('http').Server(app);
var bodyParser = require('/home/pi/app/py/flask/comm/node_modules/body-parser/');

    app.use(bodyParser.json())
    app.post('/',function(req,res){
            var msg=req.body.msg;
            console.log("python: " + msg);
    });

     http.listen(3000, function(){
     console.log('listening...');
     });