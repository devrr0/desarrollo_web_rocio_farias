const redirectIndex = () => {
    window.location.href = "../html/index.html";
}

let btnBack = document.getElementById("btn-back");
btnBack.addEventListener("click", redirectIndex);