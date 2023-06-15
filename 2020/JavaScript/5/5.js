const main = () => {
    const fs = require("fs");
    const path = require("path");

    const pathToInput = path.join(__dirname, "test.txt");
    const input = fs.readFileSync(pathToInput, "utf-8").split("\n");
    const inputLength = input.length;
    let radX = [];
    let rad = [];
    let radMax;
    let radMin;
    let kolumnX = [];
    let kolumn = [];
    let kolumnMax;
    let kolumnMin;
    let seatID = [];

    for (let i = 0; i < inputLength; i++) {
        radX.push(input[i].split(""));
    };

    for (let i = 0; i < inputLength; i++) {
        radMax = 128;
        radMin = 0;
        for (let c = 0; c < 7; c++) {
            if (radX[i][c] === "F") {
                radMax = radMax - (radMax - radMin) / 2;
            } else {
                radMin = radMin + (radMax - radMin) / 2;
            };
        };
        rad[i] = radMax - 1;
    };

    for (let i = 0; i < inputLength; i++) {
        kolumnMax = 8;
        kolumnMin = 0;
        for (let c = 7; c < 9; c++) {
            if (radX[i][c] === "L") {
                kolumnMax = kolumnMax - kolumnMin + 1;
            } else {
                kolumnMin = kolumnMin + (kolumnMax - kolumnMin) / 2 + 1;
            };//L = 0, R = 1. 101
        };
        kolumn[i] = kolumnMin;
    };

    for (let i = 0; i < inputLength; i++) {
        seatID[i] = rad[i] * 8 + kolumn[i];
    };

    //console.log(input, rad, kolumn, seatID);

    rad.sort((a, b) => a - b);
    
    const arrayToTxtFile = require('array-to-txt-file')

    arrayToTxtFile(rad, './test-output.txt', err => {
        if(err) {
          console.error(err)
          return
        }
        console.log('Successfully wrote to txt file')
    })
}



main();