const http = require("http");

const fs = require("fs");
const querystring = require("querystring");
const server = http.createServer(function (req, res) {
  console.log("Running...");
  if (req.method === "GET" && req.url === "/") {
    fs.readFile("code-injection.html", (err, data) => {
      if (err) {
        res.writeHead(500, { "Content-Type": "text/plain" });
        res.end("Internal Server Error");
      } else {
        res.writeHead(200, { "Content-Type": "text/html" });
        res.end(data);
      }
    });
  } else if (req.method === "POST" && req.url === "/") {
    let body = "";
    req.on("data", (chunk) => {
      body += chunk.toString();
    });

    req.on("end", () => {
      const formData = querystring.parse(body);
      console.log("Received form data:", formData);

      res.writeHead(200, { "Content-Type": "text/html" });
      res.end(`<p>Message: ${formData.message}!</p>`);
    });
  } else {
    // Serve other content or respond with 404
    console.log("Received something: url: ", req.url);

    res.writeHead(200, { "Content-Type": "text/html" });
    res.end("Hello World!");
  }
});

server.listen(8080);
