const fs = require("fs");

function input() {
  return fs.readFileSync(0, 'utf8')
      .trim()
}

function solve(input) {
  const [text, index] = input.split('\n');
  return text[Number(index) - 1];
}

if (require.main === module) {
  console.log(solve(input()))
}

module.exports = {solve};
