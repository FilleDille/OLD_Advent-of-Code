const fs = require("fs");
//const path = require("path");
const pathToInput = path.join(__dirname, "input.txt");
const input = fs.readFileSync(pathToInput, "utf-8").split("\n").map(inp => parseInt(inp));

function part1() {
    let nmbr;

    input.forEach((num, i) => {
        for (let c = 0; c < input.length; c++) {
            nmbr = 2020 - num - input[c + 1];
            if (input.includes(nmbr) === true) {
                console.log(input[i]);
            };
        }
        i++;
    });
};

part1();