const target = document.getElementById('target');
const lists = ['First Item', 'Second Item', 'Third Item'];
for (const name of lists) {
    const li = document.createElement('li');
    li.textContent = name;
    target.appendChild(li);
}
target.children[1].classList.add('my-item');
