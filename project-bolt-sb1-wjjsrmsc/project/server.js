const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());
app.use(express.static('public'));

let locations = new Map();

app.post('/location', (req, res) => {
    const { id, lat, lng } = req.body;
    locations.set(id, { lat, lng, timestamp: Date.now() });
    res.json({ success: true });
});

app.get('/location/:id', (req, res) => {
    const location = locations.get(req.params.id);
    if (location) {
        res.json(location);
    } else {
        res.status(404).json({ error: 'Location not found' });
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});