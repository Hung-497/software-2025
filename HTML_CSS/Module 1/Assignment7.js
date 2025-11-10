const numbers = parseInt(prompt('How many times you want to roll the dice.'));
let total = 0;

for (let i = 0; i < numbers; i++) {
  const dice = Math.floor(Math.random() * 6) + 1;
  total += dice;
  console.log(`The sum is ${total}`);
}
document.querySelector('#target').innerText = `The sum is ${total}`