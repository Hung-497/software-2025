'use strict';
const name = prompt('Enter your name below.')
const number = Math.floor(Math.random() * 4) + 1;
let house
switch (number) {
  case 1:
    house = 'Ravenclaw';
    break;
  case 2:
    house = 'Hufflepuff';
    break;
  case 3:
    house = 'Slytherin';
    break;
  case 4:
    house = 'Gryffindor';
    break;
}
document.querySelector('#target').textContent = `${name}, you are ${house}.`