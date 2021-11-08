var http = require("http");
var data = require("/Users/lukeb/it3038c-scripts-1/node/data/widgets.json")

function listBlue(res) {
    var colorBlue = data.filter(function(item) {
        return item.color === "blue"
    })
    res.end(JSON.stringify(colorBlue));
}
var server = http.createServer(function(req, res){
    if (req.url === "/") {
        res.writeHead(200, {"Content-Type": "text/json"});
        res.end(JSON.stringify(data));
    }
    else if (req.url === "/blue") {
        listBlue(res)
    }
    else {
        res.writeHead(404, {"Content-Type": "text/json"});
        res.end("404 Data not found");
    }
});

server.listen(3000)
console.log("Server is listening on port 3000");