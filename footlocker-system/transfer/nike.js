/*
	Response header info:
	Access-Control-Allow-Origin:*
	Content-Type:text/json
	X-Powered-By:nodejs
*/

var http 	= require('http');
var fs 		= require('fs');
var port 	= "8080" ;
var qs = require('querystring');


http.createServer(function(request, response) {
    var acknowledge = {actionitem: 'order', status: 'received'};
    var str_acknowledge = JSON.stringify(acknowledge);      
    response.writeHead(200, {
        'Content-Type': 'text/json',
		'Access-Control-Allow-Origin': '*',
		'X-Powered-By':'nodejs'
    });

    if (request.method == 'POST') {
        whole = ''
        request.on('data', (chunk) => {
            // consider adding size limit here
            whole += chunk.toString()
        })

        request.on('end', () => {
            const obj = JSON.parse(whole);
            console.log(obj)
            response.writeHead(200, 'OK', {'Content-Type': 'text/html'})
            response.end("UPDATE replenishment SET status = 'Order received' WHERE status = 'confirming'")
        })

    };
    console.log('order received!');


    const mysql = require('mysql');

    // First you need to create a connection to the database
    // Be sure to replace 'user' and 'password' with the correct values
    const con = mysql.createConnection({
      host: 'localhost',
      port: '8081',
      user: 'root',
      password: '',
      database: 'supplier',
    });

    con.connect(function(err)
    {
        if(err)
        {
            console.log(err);
        }
        else{
            console.log("connected")
            
            var query = "INSERT INTO reple_order (`item`, `type`, `supply_demand`, `shop`) VALUES ?";
            const obj = JSON.parse(whole);
            console.log(obj[0].item_no)
            var values = [
                [obj[0].item_name, obj[0].item_type, obj[0].supply_demand, obj[0].shop]
            ];
            con.query(query, [values], function(err, result){
                if(err)
                {
                    console.log(err);
                }
                else{
                    console.log("total enter rows = " + result.affectedRows);
                }
            })
        }
    })
//
//
//
//


}).listen(port);
console.log("Listening on port " + port );