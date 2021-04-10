var http = require("http");


var options = {
    host: "18.222.113.202",
    path: "/oss/v1/buckets",
    body: JSON.stringify({'action':'sendorder'}), 
    method: "POST",
    headers: {
        "Content-Type": "application/json"        
    }
};

var bucket = {};
bucket.name = "shiyas-bucket";

var options = {
    host: "localhost",
    port: "8080", 
    method: "POST", 
    headers: {
        "Content-Type": "application/octet-stream"
        
    }
};

var req = http.request(options, function (res) {
    var responseString = "";

    res.on("data", function (data) {
        responseString += data;
        // save all the data from response
    });
    res.on("end", function () {
        console.log(responseString); 
        // print to console when response ends
        var mysql = require('mysql');

        var con = mysql.createConnection({
          host: "localhost",
          port: '8081',
          user: 'root',
          password: '',
          database: 'footlocker',
        });

        con.connect(function(err) {
          if (err) throw err;
          con.query(responseString, function (err, result) {
            if (err) throw err;
            console.log(result.affectedRows + " record(s) updated");
          });
        });
    });
});

/*var data = require('./footlocker.json');

let userorder = data.order[0]*/

const mysql = require('mysql');

// First you need to create a connection to the database
// Be sure to replace 'user' and 'password' with the correct values
const con = mysql.createConnection({
  host: 'localhost',
  port: '8081',
  user: 'root',
  password: '',
  database: 'footlocker',
});

con.query("SELECT * FROM replenishment where status = 'confirming'", (err,rows) => {
  if(err) throw err;

  console.log('Data received from Db:');
  console.log("Order Placed", rows)

  var reqBody = JSON.stringify(rows);
  req.write(reqBody);
  req.end();

});

