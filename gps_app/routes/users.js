var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
	res.sendfile('../views/chat.html');
});

module.exports = router;
