
/**
 * Module dependencies.
 */

var express = require('express')
  , routes = require('./routes')
  , mongoose = require('mongoose');

var app = module.exports = express.createServer();

// Configuration

app.configure(function(){
  app.set('views', __dirname + '/views');
  app.set('view engine', 'ejs');
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(app.router);
  app.use(express.static(__dirname + '/public'));
});

app.configure('development', function(){
  app.use(express.errorHandler({ dumpExceptions: true, showStack: true }));
});

app.configure('production', function(){
  app.use(express.errorHandler());
});

// Routes

app.get('/', routes.index);

app.listen(3000, function(){
  console.log("Express server listening on port %d in %s mode", app.address().port, app.settings.env);
});

// DB

var Schema = mongoose.Schema;
var UserSchema = new Schema({
	u_id: String, 
	name: String,
	g_id: String,
	lat:  String,
	long: String
});
mongoose.model('User',UserSchema);
mongoose.connect('mongodb://localhost/chat_app');
var User = mongoose.model('User');


//socket

var io = require('socket.io').listen(app);
io.sockets.on('connection', function (socket) {
	socket.on('gps update',function(){
		User.find(function(err,docs){
			socket.emit('msg opne',docs);
			});
	});
	socket.on('msg send', function (msg) {
		socket.emit('msg push', msg);
		socket.broadcast.emit('msg push', msg);
		//登録
		var user =new User();
		user.u_id = msg.u_id;
		user.name = msg.name;
		user.g_id = msg.g_id;
		user.lat = msg.lat;
		user.long = msg.long;
		user.save(function(err){
			if (err){console.log(err)}
			});
	});
	//DBにあるメッセージを削除
	socket.on('deleteDB', function(drop_user){
		socket.emit('db drop');
		socket.broadcast.emit('db drop');
		User.find().remove();
		});
	  
	socket.on('disconnect', function() {
		console.log('disconnected');
	});
});

