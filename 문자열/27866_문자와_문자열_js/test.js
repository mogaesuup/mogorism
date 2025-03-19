const {solve} = require("./solution_function");
const {runSolution} = require('../../util/test_runner');

const testCases = [
  {input: "Baekjoon\n1\n", expected: "B"},
  {input: "Baekjoon\n4\n", expected: "k"},
  {input: "Hello\n2\n", expected: "e"},
  {input: "Python\n1\n", expected: "P"},
  {input: "algorithm\n5\n", expected: "r"},
  {input: "contest\n7\n", expected: "t"},
  {input: "developer\n4\n", expected: "e"},
  {input: "acmicpc\n3\n", expected: "m"},
  {input: "example\n2\n", expected: "x"},
  {input: "random\n6\n", expected: "m"},
  {input: "testing\n4\n", expected: "t"},
  {input: "pytest\n3\n", expected: "t"},
  {input: "solution\n8\n", expected: "n"},
  {input: "keyboard\n5\n", expected: "o"},
  {input: "monitor\n2\n", expected: "o"},
  {input: "laptop\n1\n", expected: "l"},
  {input: "desktop\n7\n", expected: "p"},
  {input: "internet\n4\n", expected: "e"},
  {input: "programming\n6\n", expected: "a"},
  {input: "challenge\n9\n", expected: "e"},
];

describe("function solution test", () => {
  testCases.forEach(({input, expected}, index) => {
    test(`Test case #${index + 1}`, () => {
      expect(solve(input)).toBe(expected);
    });
  });
});


describe("solution test", () => {
  testCases.forEach(({input, expected}, index) => {
    test(`Test case #${index + 1}`, async () => {
      const output = await runSolution(input, __dirname, 'solution.js');
      expect(output).toBe(expected + '\n');
    });
  });
});

describe("solution readline test", () => {
  testCases.forEach(({input, expected}, index) => {
    test(`Test case #${index + 1}`, async () => {
      const output = await runSolution(input, __dirname, 'solution_readline.js');
      expect(output).toBe(expected + '\n');
    });
  });
});
