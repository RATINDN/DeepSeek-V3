const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const app = express();
const port = 5000;

app.use(bodyParser.json());

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

// Serve the index.html file at the root URL
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.post('/generate', (req, res) => {
    const { prompt, max_new_tokens, temperature } = req.body;
    // Placeholder for model inference logic
    const completion = `Generated text for prompt: ${prompt}`;
    res.json({ completion });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});