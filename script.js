// script.js
let firstNumber = null;
let currentNumber = '';
let operation = null;

function add(n1, n2) {
    return n1 + n2;
}

function subtract(n1, n2) {
    return n1 - n2;
}

function multiply(n1, n2) {
    return n1 * n2;
}

function divide(n1, n2) {
    return n2 === 0 ? 'Error' : n1 / n2;
}

const operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
};

function appendNumber(num) {
    if (operation && currentNumber === '') {
        // If an operation is chosen, start fresh for the second number
        currentNumber = '' + num;
    } else {
        // Otherwise, append to the current number
        currentNumber += num;
    }
    updateDisplay(currentNumber);
}

function clearDisplay() {
    firstNumber = null;
    currentNumber = '';
    operation = null;
    updateDisplay('');
}

function chooseOperation(op) {
    if (currentNumber === '' && firstNumber !== null) {
        operation = op; // Change operation if already continuing with a result
        return;
    }

    if (firstNumber === null) {
        firstNumber = parseFloat(currentNumber);
    } else if (currentNumber !== '') {
        calculate(); // Perform calculation before chaining operations
    }

    operation = op;
    currentNumber = '';
}

function calculate() {
    if (firstNumber === null || currentNumber === '' || operation === null) return;

    const secondNumber = parseFloat(currentNumber);
    let result = operations[operation](firstNumber, secondNumber);

    if (result === 'Error') {
        alert("Division by zero is not allowed.");
        clearDisplay();
        return;
    }

    updateDisplay(result);
    firstNumber = result; // Use result for the next calculation
    currentNumber = ''; // Reset current number for chaining
    operation = null; // Allow user to pick a new operation
}

function updateDisplay(value) {
    document.getElementById('display').value = value;
}
