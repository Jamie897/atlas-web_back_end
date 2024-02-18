const http = require('http');

// Create the HTTP server
const app = http.createServer((req, res) => {
    // Set the response status code to 200 (OK)
    res.statusCode = 200;
    // Set the content type to plain text
    res.setHeader('Content-Type', 'text/plain');
    // Write the response body
    res.end('Hello Holberton School!\n');
});

// Listen on port 1245
const PORT = 1245;
app.listen(PORT, () => {
    console.log(`Server is running and listening on port ${PORT}`);
});

// Export the app variable (HTTP server)
module.exports = app;
