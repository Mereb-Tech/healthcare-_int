// app.js

// A simple calculator function
function calculator(operation, num1, num2) {
  switch (operation) {
    case "add":
      return num1 + num2;
    case "subtract":
      return num1 - num2;
    case "multiply":
      return num1 * num2;
    case "divide":
      return num1 / num2;
    default:
      return "Invalid operation";
  }
}

// Example usage
const operation = process.argv[2];
const num1 = parseFloat(process.argv[3]);
const num2 = parseFloat(process.argv[4]);

const result = calculator(operation, num1, num2);
console.log(`Result: ${result}`);
