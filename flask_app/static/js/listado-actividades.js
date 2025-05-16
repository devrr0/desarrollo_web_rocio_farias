const redirectIndex = () => {
    window.location.href = "../html/index.html";
}

const redirectInfo = (id) => {
    window.location.href = "/activitie/${id}";
}

let btnBack = document.getElementById("btn-back");
btnBack.addEventListener("click", redirectIndex);