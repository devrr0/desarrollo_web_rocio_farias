//redireccionar
const redirectList = () => {
    window.location.href = "../html/listado-actividades.html";
}

const redirectStats = () => {
    window.location.href = "../html/stats.html";
}

let btnList = document.getElementById("btn-list");
let btnStats = document.getElementById("btn-stats");

btnList.addEventListener("click", redirectList);
btnStats.addEventListener("click", redirectStats);