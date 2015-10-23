$(function() {

var socket = io.connect('http://localhost');
	socket.on('connect', function() { // 2
		console.log('connected');
	});
	
	$('#btn').click(function() {
		var u_id = $('#u_id');
		var name = $('#name');	 
		var g_id = $('#g_id');
		var lat = $('#lat');
		var long = $('#long');
	//	console.log(u_id);
		socket.emit('msg send', {u_id:u_id.val(),name:name.val(),lat:lat.val(),long:long.val()});
	});

	socket.on('msg push', function (msg) {
	//	console.log(msg);
	//	var date = new Date();
		$('#list').prepend($('<dt>' + msg.name + '</dt><dd>' + msg.lat + '</dd>'+'<dd>'+msg.long+'</dd>'));
	});
	
	socket.on('msg updateDB', function(msg){
		console.log(msg);
	});
});
