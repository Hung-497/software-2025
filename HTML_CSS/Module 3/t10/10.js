const form = document.getElementById('source')
const target = document.getElementById('target')

function get(event) {
    event.preventDefault()
    const first = (document.querySelector('input[name="firstname"]')).value
    const last = (document.querySelector('input[name="lastname"]')).value
    const result = `Your name is ${first} ${last}`
    target.innerText = result
}
form.addEventListener('submit', get)