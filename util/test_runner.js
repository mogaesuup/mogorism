const {spawn} = require('child_process');
const path = require('path');

function runSolution(input, filePath, fileName) {
  return new Promise((resolve, reject) => {
    const solutionPath = path.join(filePath, fileName);
    const proc = spawn('node', [solutionPath]);

    let stdout = '';
    let stderr = '';

    proc.stdout.on('data', (data) => {
      stdout += data;
    });

    proc.stderr.on('data', (data) => {
      stderr += data;
    });

    proc.on('error', (err) => {
      reject(err);
    });

    proc.on('close', (code) => {
      if (code !== 0) {
        reject(new Error(stderr));
      } else {
        resolve(stdout);
      }
    });

    proc.stdin.write(input);
    proc.stdin.end();
  });
}

module.exports = {runSolution};