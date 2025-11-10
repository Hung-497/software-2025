'use strict';
const number = parseInt(prompt('Enter an integer: '));
const target = document.querySelector('#target');
if (number < 2 || Number.isNaN(number)) {
  target.textContent = `${number} is not a prime number.`;
} else {
  let isprime = true;
  if (number > 2 && number % 2 === 0) {
    isprime = false;
  } else {
    for (let i = 3; i * i <= number; i++) {
      if (number % i === 0) {
        isprime = false;
        break;
      }
    }
  }
  target.textContent = `${number} is ${isprime ? '' : 'not'} a prime number.`;
}
