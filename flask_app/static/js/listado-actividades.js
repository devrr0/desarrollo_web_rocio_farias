const redirectIndex = () => {
    window.location.href = "../home";
}

const redirectInfo = (id) => {
    window.location.href = "/activitie/"+id;
}

let btnBack = document.getElementById("btn-back");
btnBack.addEventListener("click", redirectIndex);