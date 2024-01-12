#!/usr/bin/node
function factorial (n) {
  return n <= 1 ? 1 : n * factorial(n - 1);
}
const arg = parseInt(process.argv[2]) || 1;
console.log(factorial(arg));
