const number = parseInt(prompt('The number of participants'));
const list = [];
const target = document.getElementById('target')

if (Number.isNaN(number)) {
  target.textContent = 'please enter a valid number'
} else {
  for (let i = 0; i < number; i++) {
    const name = prompt('Enter name of the participants.');
    list.push(name);
  }
}
const lists = list.sort()
const ol = document.createElement('ol');
for (const name of lists) {
  const li = document.createElement('li');
  li.textContent = name;
  ol.appendChild(li);
}
target.replaceChildren(ol);
