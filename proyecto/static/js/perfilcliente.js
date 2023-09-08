const imgUser = document.querySelector('#imgUser');
const alertAsk = document.querySelector('#alertAsk');
const btnA = document.querySelector('#btnA');
const btnC = document.querySelector('#btnC')

$(window).load(function() {
    $(".loader").fadeOut("slow");
});

function ocultar(){
    alertAsk.style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function(){
    ocultar()
})



imgUser.addEventListener('click', function(){
    
    alertAsk.style.display = 'block';
    alertAsk.style.display = 'flex';
});

btnC.addEventListener('click', function(){
    alertAsk.style.display = 'none'
})