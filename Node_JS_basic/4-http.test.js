const assert = require('assert');
const axios = require('axios');
const app = require('./4-http');

describe('HTTP Server', () => {
    // Start the HTTP server before running the tests
    before(() => {
        app.listen(1245);
    });

    // Stop the HTTP server after running the tests
    after(() => {
        app.close();
    });

    it('responds with correct content and status code for root endpoint', async () => {
        try {
            // Make a GET request to the root endpoint
            const response = await axios.get('http://localhost:1245');
            
            // Assert the status code is 200 (OK)
            assert.strictEqual(response.status, 200);

            // Assert the response body contains the correct content
            assert.strictEqual(response.data, 'Hello Holberton School!\n');
        } catch (error) {
            // If an error occurs, fail the test and log the error
            assert.fail(error.message);
        }
    });
});
