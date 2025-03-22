const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
const [text, index] = input.split('\n');
console.log(text[Number(index) - 1]);