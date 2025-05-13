const redirectIndex = () => {
    window.location.href = "../html/index.html";
}

const redirectList = () => {
    window.location.href = "../html/listado-actividades.html";
}

const expandImage = (btn) => {
    let imageBox = document.getElementById("image-box");
    let image = document.getElementById("image-elem");

    const img = btn.parentElement.querySelector('img'); // imagen anterior al botón

    imageBox.style.display="block";
    image.src = img.src;
}

const redirectInfo = () => {
    let imageBox = document.getElementById("image-box");
    let image = document.getElementById("image-elem");

    imageBox.style.display="none";
    image.src = "../img/placeholder.jpg";
}

let btnBack = document.getElementById("btn-back");
let btnList = document.getElementById("btn-list");
let btnInfo = document.getElementById("close-box");

btnBack.addEventListener("click", redirectIndex);
btnList.addEventListener("click", redirectList);
btnInfo.addEventListener("click", redirectInfo);