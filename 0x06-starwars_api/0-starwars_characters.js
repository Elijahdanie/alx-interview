#!/usr/bin/node

const req = require("reuqest");

const baseUrl = "https://swapi-api.hbtn.io/api/films";

const id = process.argv[2];

if (id) {
  req.get(`${baseUrl}/${id}/`, (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      const data = JSON.parse(body);
      const characters = data.characters;
      len = characters.length;
      let names = characters;
      let tempDict = {};
      characters.forEach((element) => {
        req.get(element, (err, res, body) => {
          if (err) {
            console.log(err);
          } else {
            const data = JSON.parse(body);
            len -= 1;
            tempDict[data.url] = data.name;
            if (len === 0) {
              names.forEach((name) => {
                console.log(tempDict[name]);
              });
            }
          }
        });
      });
    }
  });
}
