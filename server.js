const http = require('http');

const port = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
    console.log("Request received at:", new Date());

    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello from Saikanth Backend App 🚀');
});

server.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
