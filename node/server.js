var fs = require("fs");
var http = require('http');
var ip = require('ip');
var os = require('os');
function format(seconds){
    function pad(s){
      return (s < 10 ? '0' : '') + s;
    }
    var hours = Math.floor(seconds / (60*60));
    var minutes = Math.floor(seconds % (60*60) / 60);
    var seconds = Math.floor(seconds % 60);
  
    return pad(hours) + ':' + pad(minutes) + ':' + pad(seconds);
  }
  
var uptime = process.uptime();
console.log(format(uptime));

console.log('RAM: ', os.totalmem());
console.log('Free RAM: ', os.freemem());

const cpuCount = os.cpus().length

var server = http.createServer(function(req, res){
    if (req.url === "/") {
        fs.readFile("./public/index.html", "utf-8", function(err, body){
            res.writeHead(200, {"Content-Type":"text/html"});
            res.end(body);
        });
    }
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        html = `
        <!DOCTYPE html>
        <html>
            <head>
                <title>Node JS Response</title>
                </head>
                <body>
                <p>Hostname: ${myHostName}</p>
                <p>IP: ${ip.address()}</p>
                <p>Server Uptime: ${format(uptime)}</p>
                <p>Total Memory: ${os.totalmem()}</p>
                <p>Free Memory: ${os.freemem()}</p>
                <p>Number of CPUs: ${os.cpus().length}</p>
                </body>
        </html>    
        `
       res.writeHead(200, {"Content-Type":"text/html"});
       res.end(html);
    }

    else {
        res.writeHead(404, {"Content-Type": "text/html"})
        res.end(`404 file not found at ${req.url}`);
    }
});

server.listen(3000);

console.log("Server lisetening on port 3000");