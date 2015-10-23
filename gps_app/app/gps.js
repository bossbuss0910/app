var mysql = require('mysql');


var gpsSchema = new mysql.Schema({
	users : {
		u_id:{type:'increments',nullable:false,primary:true}
		name:{type:'string',maxlength:100,nullable:false}
		}
});


