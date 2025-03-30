const redirectIndex = () => {
    window.location.href = "../html/index.html";
}

const redirectInfo = () => {
    window.location.href = "../html/info-app.html";
}

let btnBack = document.getElementById("btn-back");
btnBack.addEventListener("click", redirectIndex);