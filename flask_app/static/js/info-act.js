
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

const validateForm = (nombre, comentario) => {
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
    return { nombre: nombre.value, comText: comentario.value, isValid: isValid };
}

let myForm = document.forms["myForm"];
let nombreInput = myForm["nombre"];
let comentarioInput = myForm["comentario"];
let act_id = myForm["act_id"].value;
const agregarComentario = () => {
    let { nombre, comText, isValid } = validateForm(nombreInput, comentarioInput);
    if (!isValid){
        document.getElementById("problem-msg").innerText = "Hay problemas con el formulario";
        return;
    } 
    fetch(myForm.action, {
        method: "POST",
        body: JSON.stringify({ nombre:nombre, comText: comText, act_id: act_id}),
        credentials: "include",
        cache: "no-cache",
        headers: {
            "Content-Type": "application/json",
        },
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error("Error uploading forms");
        }
    })
    .then(data => {
        document.getElementById("problem-msg").innerText = "Comentario agregado correctamente";
        myForm.reset();
    })
    .catch((error) => {
      console.error(
        "There has been a problem with your fetch operation:",
        error
      );
    });
}


let btnInfo = document.getElementById("close-box");
let btnForms = document.getElementById("btn-add-com")

btnForms.addEventListener("click", agregarComentario)
btnInfo.addEventListener("click", redirectInfo);