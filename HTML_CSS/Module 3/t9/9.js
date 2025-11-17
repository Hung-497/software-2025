const inp = document.getElementById('calculation')
const but = document.getElementById('start')
const re = document.getElementById('result')

function cal() {
    const calculation = inp.value.split(' ').join('');
    console.log(calculation);
    if (calculation.includes('+')) {
        const parts = calculation.split('+');
        const a = Number(parts[0])
        const b = Number(parts[1])
        const result = a + b 
        re.innerText = `Result is ${result}`
    } else if (calculation.includes('-')) {
        const parts = calculation.split('-');
        const a = Number(parts[0])
        const b = Number(parts[1])
        const result = a - b 
        re.innerText = `Result is ${result}`
    } else if (calculation.includes('*')) {
        const parts = calculation.split('*');
        const a = Number(parts[0])
        const b = Number(parts[1])
        const result = a * b
        re.innerText = `Result is ${result}`
    } else if (calculation.includes('/')) {
        const parts = calculation.split('/');
        const a = Number(parts[0])
        const b = Number(parts[1])
        const result = a / b
        re.innerText = `Result is ${result}`
    } else {
        re.innerText = 'Please enter valid number'
    }
}
but.addEventListener('click', cal);