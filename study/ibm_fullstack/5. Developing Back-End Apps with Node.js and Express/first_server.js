const http = require("http");
const server = http.createServer((req, res) => {
  const body = "Hello World!";
  res.writeHead(200, {
    "Content-Length": body.length,
    "Content-Type": "text/plain",
  });
  res.end(body);
});

server.listen(8080);
