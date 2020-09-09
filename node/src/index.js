// const http = require('http'); // Import Node.js core module
const express = require('express')
const {spawn} = require('child_process');

const app = express()
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
    res.send('Query \"/Bayes?C=1&F=0&R=1&S=0&Result=0\"')
});

app.get('/AssosiateRules', call_fn_AssosRules);
// # mongodb+srv://dmprojectadmin:<password>@dm-project.kchhf.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority
app.get('/Bayes', call_fn_Bayes);

function call_fn_AssosRules(req,res) { 
    try {
        let process = spawn('python', ["../../../w4/lect4/AssosiateRules_script.py",
            req.query.C,
            req.query.F,
            req.query.R,
            req.query.S,
            req.query.Result,
        ]);
    } catch (error) {
        console.log(`${error}`);
    }

    process.stdout.on('data', function (data) {
        res.send(data.toString());
    })
}

function call_fn_Bayes(req,res) { 
    let inputData = ["../Bayes_script.py"]
    for ( each in req.query){
        inputData.push(req.query[each]);
    }
    
    console.log(inputData)
    let process = spawn('python', ["../Bayes_script.py",
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
