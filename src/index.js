// const http = require('http'); // Import Node.js core module
const express = require('express')
const {spawn} = require('child_process');

const app = express()
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
    res.send(dataToSend)
});

app.get('/Bayes', call_f_Bayes);

function call_f_Bayes(req,res) { 
    let process = spawn('python', ["../script.py",
        req.query.C,
        req.query.F,
        req.query.R,
        req.query.S,
        req.query.Result,
    ]);

    process.stdout.on('data', function (data) {
        res.send(data.toString());
    })
}

app.listen(port, () => console.log(`Bayes app listening on port ${port}!`));
