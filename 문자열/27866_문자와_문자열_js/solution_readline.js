const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const inputs = [];

rl.on('line', (line) => {
  inputs.push(line);
  if(inputs.length === 2) {
    rl.close();
  }
})

function* getInput() {
  let i = 0;
  while (i < inputs.length) {
    yield inputs[i++];
  }
}

const solve = () => {
  const inputIter = getInput();
  const text = inputIter.next().value;
  const index = inputIter.next().value;
  console.log(text[Number(index) - 1]);
};

rl.on('close', () => {
  solve()
})
