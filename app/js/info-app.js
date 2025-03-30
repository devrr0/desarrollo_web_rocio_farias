const redirectIndex = () => {
    window.location.href = "../html/index.html";
}

const redirectList = () => {
    window.location.href = "../html/listado-actividades.html";
}

let btnBack = document.getElementById("btn-back");
let btnList = document.getElementById("btn-list");

btnBack.addEventListener("click", redirectIndex);
btnList.addEventListener("click", redirectList);