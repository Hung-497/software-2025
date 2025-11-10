'use strict';
const answer = confirm('Should I calculate the square root?');
const ok = document.querySelector('#target');

if (!answer) {
  ok.innerHTML = 'The square root is not calculated.';
} else {
  const value = parseFloat(prompt('Enter the number.'));
  if (Number.isNaN(value)) {
    ok.innerHTML('Enter the valid number.');
  } else if (value < 0) {
    ok.innerHTML('The square root of a negative number is not defined.');
  } else {
    const result = Math.sqrt(value);
    ok.innerHTML = `The square root is ${result.toFixed(2)}`;
  }
}

