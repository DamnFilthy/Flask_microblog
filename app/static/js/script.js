//   $(document).ready(function(){
// alert(jQuery.fn.jquery);
// });

window.addEventListener('load', function () {
    var but = document.getElementById('but');
    var slider = document.getElementById('box');
    but.addEventListener('click', function () {
        slider.classList.toggle('slidein');
    }, false);
}, false);