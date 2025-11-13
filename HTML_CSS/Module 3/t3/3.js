'use strict';
const names = ['John', 'Paul', 'Jones'];
for (let name of names) {
    const li = document.createElement('li');
    li.textContent = name;
    document.getElementById('target').appendChild(li);
}
