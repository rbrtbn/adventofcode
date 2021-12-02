#!/usr/bin/env npx ts-node

import * as fs from 'fs';
import { exit } from 'process';

const measurements = fs
    .readFileSync('./input.txt', 'utf-8')
    .split(/\n/)
    .filter(line => line != '')
    .map(numStr => Number(numStr));

let increments = 0;
let prev = measurements.shift()!;

measurements.forEach(current =>  {
    if (current > prev) {
        increments += 1;
    }
    prev = current;
});

console.log(increments);