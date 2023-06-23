const fs = require("fs");
const path = require("path");
const pathToInput = path.join(__dirname, "input.txt");
const input = fs.readFileSync(pathToInput, "utf-8").split("\n");
const inputLength = input.length;
const inputRoadLength = input[0].length;

function part1() {
    let road = [];
    let c = 0;
    let count = 0;

    for (let i = 0; i < inputLength; i++) {
        road[i] = input[i].split("")[c];
        if (c < 28) {
            c = c + 3;
        } else {
            if (c === 28) {
                c = 0;
            };
            if (c === 29) {
                c = 1;
            };
            if (c === 30) {
                c = 2;
            };
        };
        if (road[i] === "#") {
            count++;
        }
    };

    console.log(count);
};

function part2() {
    let road1 = [];
    let road2 = [];
    let road3 = [];
    let road4 = [];
    let road5 = [];
    let count1 = 0;
    let count2 = 0;
    let count3 = 0;
    let count4 = 0;
    let count5 = 0;
    let a = 0;
    let b = 0;
    let c = 0;
    let d = 0;
    let e = 0;

    for (let i = 0; i < inputLength; i++) {
        road1[i] = input[i].split("")[a];
        if (a < 30) {
            a = a + 1;
        } else {
            if (a === 30) {
                a = 0;
            };
        };
        if (road1[i] === "#") {
            count1++;
        };
    };

    for (let i = 0; i < inputLength; i++) {
        road2[i] = input[i].split("")[b];
        if (b < 28) {
            b = b + 3;
        } else {
            if (b === 28) {
                b = 0;
            };
            if (b === 29) {
                b = 1;
            };
            if (b === 30) {
                b = 2;
            };
        };
        if (road2[i] === "#") {
            count2++;
        };
    };

    for (let i = 0; i < inputLength; i++) {
        road3[i] = input[i].split("")[c];
        if (c < 26) {
            c = c + 5;
        } else {
            if (c === 26) {
                c = 0;
            };
            if (c === 27) {
                c = 1;
            };
            if (c === 28) {
                c = 2;
            };
            if (c === 29) {
                c = 3;
            };
            if (c === 30) {
                c = 4;
            };
        };
        if (road3[i] === "#") {
            count3++;
        };
    };

    for (let i = 0; i < inputLength; i++) {
        road4[i] = input[i].split("")[d];
        if (d < 24) {
            d = d + 7;
        } else {
            if (d === 24) {
                d = 0;
            };
            if (d === 25) {
                d = 1;
            };
            if (d === 26) {
                d = 2;
            };
            if (d === 27) {
                d = 3;
            };
            if (d === 28) {
                d = 4;
            };
            if (d === 29) {
                d = 5;
            };
            if (d === 30) {
                d = 6;
            };
        };
        if (road4[i] === "#") {
            count4++;
        };
    };

    for (let i = 0; i < inputLength; i = i + 2) {
        road5[i] = input[i].split("")[e];
        if (e < 30) {
            e++;
        } else {
            if (e === 30) {
                e = 0;
            };
        };
        if (road5[i] === "#") {
            count5++;
        };
    };

    let lol = count1 * count2 * count3 * count4 * count5;

    console.log(lol);
};

part1();