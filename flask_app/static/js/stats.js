const redirectIndex = () => {
    window.location.href = "../home";
}

let btnBack = document.getElementById("btn-back");
btnBack.addEventListener("click", redirectIndex);