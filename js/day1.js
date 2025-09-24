import fs from "fs";

const reader = (input) => {
  const esraAndMert = fs.readFileSync(input, "utf-8");
  return esraAndMert;
};

const day1 = (text) => {
  let counter = 0;
  for (let i = 0; i < text.length; i++) {
    if (text[i] == "(") counter++;
    else counter--;
  }
  return counter;
};

console.log(day1(reader("../day1.txt")));
