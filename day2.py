import fs from "fs"


const reader = (input) => {
  const inputokai = fs.readFileSync(input, "utf-8")
  return inputokai
}

console.log(reader("day1.txt"))))
