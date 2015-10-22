var configRoutes;
var mongo = require('mongodb');
configRoutes = function(app, server) {
	    app.get('/a', function(request, response) {
		            response.redirect('/index.html');
			        });

//	         パスが'/*'の場合は、jsonにして、
	    app.all('/*', function(request, response, next){
		             response.contentType('json');
		                     response.header('Access-Control-Allow-Origin', '*');
		                             next();
	                                 });
	    app.get('/find', function(request, response) {
		    mongo.find('test', {}, {}, 
		    function(list){
			    response.send(list);
			    }
			    );
		    });
	    }

module.exports = {configRoutes: configRoutes};
