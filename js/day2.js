import fs from "fs";

const reader = (path) => {
  const text = fs.readFileSync(path, "utf-8");
  const lines = text.trim().split(/\r?\n/);
  return lines;
};

const dayTwo = (input) => {
  const arr = [];
  let counter = 0;
  for (let i = 0; i < input.length; i++) {
    const array = input[i].split("x");
    arr.push(array);
  }
  for (let i = 0; i < arr.length; i++) {
    counter = calculator(arr[i]) + counter;
  }
  return counter;
};

function calculator(params) {
  const min = Math.min(
    params[0] * params[1],
    params[1] * params[2],
    params[0] * params[2],
  );
  const nums =
    2 * params[0] * params[1] +
    2 * params[1] * params[2] +
    2 * params[0] * params[2];
  return min + nums;
}

console.log(dayTwo(reader("../day2.txt")));
