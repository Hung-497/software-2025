const list = [];
const target = document.getElementById('target')
const number = 6
for (let i = 0; i < number; i++) {
    const name = prompt('Enter name of the dogs.');
    list.push(name);
  }
const lists = list.sort().reverse()
const ul = document.createElement('ul');
for (const name of lists) {
  const li = document.createElement('li');
  li.textContent = name;
  ul.appendChild(li);
}
target.replaceChildren(ul);
