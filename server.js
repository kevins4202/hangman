import express from 'express';

import path from 'path';

const app = express();

let port = process.env.PORT;
if (port == null || port == "") {
  port = 9000;
}

app.use(express.static("public"));

app.get('/', (req, res) => {
    res.render('index.ejs', {
        word: getRandomWord()
    });
});

// app.get('/word', (req, res) => {
//     res.json({ word });
// });

app.get('/restart', (req, res) => {
    res.redirect('/');
});

app.listen(port, () =>{
    console.log(`Server running on port ${port}`);
});


