
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
    image.src = "../img/placeholder.png";
}

// Validacion formulario

const validateName = (name) => {
    if(!name) return false;
    let maxValid = name.trim().length <= 80;
    let minValid = name.trim().length >= 3;
    return maxValid && minValid;
};

const validateComment = (comment) => {
    if(!comment) return false;
    let minValid = comment.trim().length >= 5;
    return minValid;
};

const validateForm = () => {
    let myForm = document.forms["myForm"];
    let nombre = myForm["nombre"];
    let comentario = myForm["comentario"];
    let problemMessageElem = document.getElementById("problem-msg");

    let isValid = true;
    if(!validateName(nombre.value)){
        nombre.style.borderColor = "red";
        isValid = false;
    } else{
        nombre.style.borderColor = "";
    }
    if(!validateComment(comentario.value)){
        comentario.style.borderColor = "red";
        isValid = false;
    } else{
        comentario.style.borderColor = "";
    }

    if (!isValid){
        problemMessageElem.innerText = "Hay problemas con el formulario";
    }
    else{
        problemMessageElem.innerText = "Se ha subido correctamente su comentario";
        myForm.submit();
    }
}

let btnInfo = document.getElementById("close-box");
let btnForms = document.getElementById("btn-add-com")

btnForms.addEventListener("click", validateForm)
btnInfo.addEventListener("click", redirectInfo);