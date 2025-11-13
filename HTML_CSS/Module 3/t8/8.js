const n1 = document.getElementById('num1');
const n2 = document.getElementById('num2');
const btn = document.getElementById('start');
const result = document.getElementById('result');
const op = document.getElementById('operation');

function cal() {
    const a = Number(n1.value)
    const b = Number(n2.value)
    let ans;
    switch (op.value) {
        case 'add': ans = a + b;
            break;
        case 'sub': ans = a - b;
            break;
        case 'multi': ans = a * b;
            break;
        case 'div': ans = a / b;
            break;
        default:
            op.innerText = 'Choose the operation';
            return;
    }
    result.textContent = `Result: ${ans}`
}
btn.addEventListener('click', cal);

