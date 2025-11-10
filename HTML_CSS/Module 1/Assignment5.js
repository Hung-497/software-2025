'use strict';
const year = parseInt(prompt('Enter a year below to check.'))
let message = '';
if (Number.isNaN(year)) {
  message = `${year} is not a number.`
} else if (year % 400 === 0) {
  message =`${year} is a leap year.`;
} else if (year % 100 === 0) {
  message = `${year} is not a leap year.`;
} else if (year % 4 === 0) {
  message =`${year} is a leap year.`;
} else {
  message = `${year} is not a leap year.`;
}
document.querySelector('#target').textContent = message

