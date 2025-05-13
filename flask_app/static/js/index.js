//redireccionar
const redirectList = () => {
    window.location.href = "../html/listado-actividades.html";
}

const redirectStats = () => {
    window.location.href = "../html/stats.html";
}

const redirectAdd = () => {
    window.location.href = "../html/agregar-actividad.html";
}

let btnList = document.getElementById("btn-list");
let btnStats = document.getElementById("btn-stats");
let btnAdd = document.getElementById("btn-add");

btnList.addEventListener("click", redirectList);
btnStats.addEventListener("click", redirectStats);
btnAdd.addEventListener("click", redirectAdd);