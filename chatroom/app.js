var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var routes = require('./app/routes');

app.use(express.static(__dirname + '/views'));

//app.get('/', function(req, res){
//	  res.sendFile(__dirname + '/views/index.html');
//});

io.on('connection', function(socket){
	socket.on('chat message',function(msg){
	io.emit('chat message', msg);
	});
});

http.listen(3000, function(){
	  console.log('listening on *:3000');
});
