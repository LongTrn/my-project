// const http = require('http'); // Import Node.js core module
const express = require('express');
const {spawn} = require('child_process');
const path = require('path');

const app = express()
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
    res.send('Query \"/Bayes?C=1&F=0&R=1&S=0&Result=0\"')
    // http://localhost:3000/AssosiateRules?options=SupportList&minsp=0.1&minconf=1
});

app.get('/AssosiateRules', call_fn_AssosRules);
// # mongodb+srv://dmprojectadmin:<password>@dm-project.kchhf.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority
app.get('/Bayes', call_fn_Bayes);

function call_fn_AssosRules(req,res) { 
    let process = spawn('python', ["../scripts/AssosiateRules_script.py",
        req.query.options, // starting funds
        req.query.minsp, // (initial) wager size
        req.query.minconf // wager count — number of wagers per sim
    ],{
        cwd: path.dirname(require.main.filename)
    });
    process.stdout.on('data', function (data) {
        res.send(data.toString());
    });
    process.stdout.on('data', function (data) {
        console.log('stdout: ' + data.toString());
    });
    
    process.stderr.on('data', function (data) {
    console.log('stderr: ' + require('path').dirname(require.main.filename));
    });
    
    process.on('exit', function (code) {
    console.log('child process exited with code ' + code.toString());
    });
}

function call_fn_Bayes(req,res) { 
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

app.listen(port, () => console.log(`Server app listening on port ${port}!`));
