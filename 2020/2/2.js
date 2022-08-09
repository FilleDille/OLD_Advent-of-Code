const fs = require("fs");
const path = require("path");
const pathToInput = path.join(__dirname, "input.txt");
const pwd = fs.readFileSync(pathToInput, "utf-8").split("\n");
const pwdLength = pwd.length;

let pwdSplit = [];
let pwdLetter = [];
let pwdMin = [];
let pwdMax = [];
let pwdNmbr = [];

function part1() {
    pwd.forEach(function (entry) {
        pwdSplit.push(entry.split(" "));
    });

    let count = 0;

    for (i = 0; i < pwdLength; i++) {
        pwdMin[i] = parseInt(pwdSplit[i][0].split("-")[0]);
        pwdMax[i] = parseInt(pwdSplit[i][0].split("-")[1]);
        pwdLetter[i] = pwdSplit[i][1].split("")[0];
        pwdNmbr[i] = pwdSplit[i][2].split('').filter(letter => (letter === pwdLetter[i])).length;
        if (pwdNmbr[i] >= pwdMin[i] && pwdNmbr[i] <= pwdMax[i]) {
            count++;
        };
    };

    console.log(count);
};

function part2() {
    pwd.forEach(function (entry) {
        pwdSplit.push(entry.split(" "));
    });

    let count = 0;
    let pwd1 = [];

    for (i = 0; i < pwdLength; i++) {
        pwdMin[i] = parseInt(pwdSplit[i][0].split("-")[0]);
        pwdMax[i] = parseInt(pwdSplit[i][0].split("-")[1]);
        pwdLetter[i] = pwdSplit[i][1].split("")[0];
        pwd1[i] = pwdSplit[i][2].split("");
        if (pwd1[i][pwdMin[i] - 1] === pwdLetter[i]) {
            if (pwd1[i][pwdMax[i] - 1] === pwdLetter[i]) {
            } else {
                count++;
            };
        } else {
            if (pwd1[i][pwdMax[i] - 1] === pwdLetter[i]) {
                count++;
            };

        };
    };

    console.log(count);
};

part2();
