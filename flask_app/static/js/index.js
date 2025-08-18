//redireccionar
const redirectList = () => {
    window.location.href = "../list-activities";
}

const redirectStats = () => {
    window.location.href = "../stats";
}

const redirectAdd = () => {
    window.location.href = "../post-activitie";
}

let btnList = document.getElementById("btn-list");
let btnStats = document.getElementById("btn-stats");
let btnAdd = document.getElementById("btn-add");

btnList.addEventListener("click", redirectList);
btnStats.addEventListener("click", redirectStats);
btnAdd.addEventListener("click", redirectAdd);