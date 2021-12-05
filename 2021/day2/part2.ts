#!/usr/bin/env node --loader ts-node/esm

import { fetchInput } from "../utils.js";

const input = await fetchInput(2);

const moves = input.trim().split("\n");

let horizontal = 0;
let depth = 0;
let aim = 0;

moves.forEach(move => {
    const [direction, value] = move.split(' ');
    switch(direction) {
        case 'forward':
            horizontal += parseInt(value);
            depth += aim * parseInt(value);
            break;
        case 'up':
            aim -= parseInt(value);
            break;
        case 'down':
            aim += parseInt(value);
            break;
    }
});

console.log(horizontal, depth, horizontal * depth);