'use strict';

let inputs = [];
for (let i = 0; i < 5; i++) {
  inputs.push(parseInt(prompt('Enter your number'),10 ));
}
for (let i = inputs.length - 1; i >= 0; i--) {
  console.log(inputs[i]);
}
