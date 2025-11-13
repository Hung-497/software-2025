const target = document.querySelector('#trigger');
const pic = document.querySelector('#target');

target.addEventListener('mouseover', () => {
    pic.src ='img/picB.jpg';
});
target.addEventListener('mouseout', () => {
   pic.src ='img/picA.jpg';
}); 
