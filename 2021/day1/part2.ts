#!/usr/bin/env npx ts-node

import * as fs from 'fs';
import { exit } from 'process';

const measurements = fs
    .readFileSync('./input.txt', 'utf-8')
    .split(/\n/)
    .filter(line => line != '')
    .map(numStr => parseInt(numStr));

const sum = (arr: number[]) => arr.reduce((pv, cv) => pv + cv, 0);

const windowSize = 3;
let increments = 0;
let prev = sum(measurements.slice(0, windowSize));

measurements.slice(windowSize).forEach((v, i) => {
    const current = prev + v - measurements[i];
    if (current > prev) increments += 1;
    prev = current;
});

console.log(increments);