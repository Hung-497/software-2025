'use strict';
const a = parseInt(prompt('Type your first number.'));
const b = parseInt(prompt('Type your second number.'));
const c = parseInt(prompt('Type your third number.'));
const sum = a + b + c
const product = a*b*c
const average= sum /3
const box = document.querySelector('#target');
box.innerHTML = `
<p>First number: ${a}, Second number: ${b}, Third number: ${c}</p>
<ul>
<li>Sum: ${sum}</li>
<li>Product: ${product}</li>
<li>Average: ${average.toFixed(2)}</li>
</ul>`;
