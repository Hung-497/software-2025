'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const target = document.getElementById('target')
students.forEach(stu => {
  const student = document.createElement('option')
  student.innerText = stu.name
  student.value = stu.id
  target.appendChild(student)
}
);



