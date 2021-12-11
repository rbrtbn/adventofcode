#!/usr/bin/env node --loader ts-node/esm

import { exit } from "process";
import { fetchInput } from "../utils.js";

const input = await fetchInput(8);

const filterBySegmentCount = (count: number) => (segments: string) => segments.length === count;
const overlapsWith = (segmentsToFind: string) => (segments: string) => segments.match(new RegExp(`[${segmentsToFind}]`, "g")).length === segmentsToFind.length;
const not = (fn: (segments: string) => boolean) => (segments: string) => !fn(segments);

let count1478 = 0;
let sum = 0;

input.split("\n").forEach(line => {
  if (line == "") return;

  const [numberList, code] = line.split("|").map(str =>
    str
      .trim()
      .split(" ")
      .map(str => str.split("").sort().join(""))
  );

  const numberMap: { [key: number]: string } = {};
  numberMap[1] = numberList.find(filterBySegmentCount(2));
  numberMap[4] = numberList.find(filterBySegmentCount(4));
  numberMap[7] = numberList.find(filterBySegmentCount(3));
  numberMap[8] = numberList.find(filterBySegmentCount(7));

  const numbers1478 = [numberMap[1], numberMap[4], numberMap[7], numberMap[8]];

  const numbers069 = numberList.filter(filterBySegmentCount(6));
  numberMap[6] = numbers069.find(not(overlapsWith(numberMap[1])));

  const numbers09 = numbers069.filter(number => number !== numberMap[6]);
  const lettersBD = numberMap[4].split("").filter(letter => !numberMap[1].includes(letter));
  const lettersED = numbers09[0]
    .split("")
    .filter(letter => !numbers09[1].includes(letter))
    .concat(numbers09[1].split("").filter(letter => !numbers09[0].includes(letter)));
  const letterD = lettersED.filter(letter => lettersBD.includes(letter)).join("");

  numberMap[9] = numbers09.find(number => number.includes(letterD));
  numberMap[0] = numbers09.find(number => !number.includes(letterD));

  const numbers235 = numberList.filter(filterBySegmentCount(5));

  numberMap[3] = numbers235.find(overlapsWith(numberMap[1]));
  numberMap[5] = numbers235.find(number => overlapsWith(number)(numberMap[6]));
  numberMap[2] = numbers235.find(number => number !== numberMap[3] && number !== numberMap[5]);

  count1478 += code.filter(number => numbers1478.includes(number)).length;

  const reverseMap = {};
  Object.keys(numberMap).forEach(num => (reverseMap[numberMap[num]] = num));

  sum += parseInt(code.map(number => reverseMap[number]).join(""));
});

console.log(count1478, sum);
