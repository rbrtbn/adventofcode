#!/usr/bin/env node --loader ts-node/esm

import { fetchInput } from "../utils.js";

const input = await fetchInput(2);

const moves = input.trim().split("\n");

let horizontal = 0;
let depth = 0;

moves.forEach(move => {
    const [direction, value] = move.split(' ');
    switch(direction) {
        case 'forward':
            horizontal += parseInt(value);
            break;
        case 'up':
            depth -= parseInt(value);
            break;
        case 'down':
            depth += parseInt(value);
            break;
    }
});

console.log(horizontal, depth, horizontal * depth);