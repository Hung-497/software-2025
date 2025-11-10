'use strict';
const start = parseInt(prompt('Enter the start year below.'))
const end = parseInt(prompt('Enter the end year below.'))
const years = []
const target = document.querySelector('#target');
for (let y = start; y<=end;y++) {
  if (Number.isNaN(start) || Number.isNaN(end)) {
  target.innerText = 'Please enter valid years.'
} else if (y % 400 === 0) {
  years.push(y)
} else if (y % 100 === 0) {
  continue;
} else if (y % 4 === 0) {
  years.push(y)
} else {
  continue;
}
}
target.innerHTML = `<ul>${years.map(y => `<li>${y}</li>`).join('')}</ul>`;
