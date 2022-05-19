#!/usr/bin/node

const req = require("reuqest");

const baseUrl = "https://swapi-api.hbtn.io/api/films";

const id = process.argv[2];
var names = []
var len = 0;
var tempDict = {}

if (id) {
   req.get(`${baseUrl}/${id}/`, (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      const data = JSON.parse(body);
      const characters = data.characters;
      len = characters.length;
      names = characters;
      characters.forEach((element) => {
        req.get(element, (err, res, body) => {
          if (err) {
            console.log(err);
          } else {
            const data = JSON.parse(body);
            track(data.name, data.url);
          }
        });
      });
    }
  });
}

function track(n, url)
{
    len -=1;
    tempDict[url] = n;
    if (len == 0)
    {
        names.forEach(name =>{
            console.log(tempDict[name]);
        })
    }
}
