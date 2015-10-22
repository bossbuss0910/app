var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
	res.sendfile('chat.html');
});

router.on('connection', function(socket){
	  socket.on('chat message', function(msg){
		      console.log('message: ' + msg);
		        });
});

module.exports = router;
