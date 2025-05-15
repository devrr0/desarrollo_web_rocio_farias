
const redirectIndex = () => {
    window.location.href = "../html/index.html";
};

// Validacion Region y Comuna
const validateSelect = (select) => {
    if(!select) return false;
    return true
};

// Validacion Sector
const validateSector = (sector) => {
    let lengthValid = sector.trim().length <= 100;
    return lengthValid;
};

// Validacion Nombre Organizacion
const validateName = (name) => {
    if(!name) return false;
    let maxValid = name.trim().length <= 200;
    let minValid = name.trim().length >= 3;
    return maxValid && minValid;
};

// Validacion Email
const validateEmail = (email) => {
    if (!email) return false;
    let minValid = email.length > 10;
    let maxValid = email.length <= 100;
  
    // validación de formato
    let re = /^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    let formatValid = re.test(email);
  
    return minValid && maxValid && formatValid;
};

// Validacion Telefono
const validatePhoneNumber = (phoneNumber) => {
    let lengthValid = phoneNumber.length == 12;
  
    // validación de formato
    let re =  /^\+569\d{8}$/; 
    let formatValid = re.test(phoneNumber);
  
    return lengthValid && formatValid;
};

// Validacion Contacto
const validateContact = (input, contact_number) => {
    // recorrrer la lista de info de contacto y checkear el largo de c/u
    let minLength = input >= 4;
    let maxLength = input <= 50;
    let max_contacts = contact_number <= 5;
    
    return minLength && maxLength && max_contacts;
};

// Validacion Fecha Inicio
const validateInitTime = (time) => {
    if(!time) return false;
    const now = new Date();
    const date = new Date(time);
    let minTime = now < date;
    return minTime
}

// Validacion Fecha Termino
const validateEndTime = (initTime, endTime) => {
    const init = new Date(initTime);
    const end = new Date(endTime)

    let minTime = init < end;
    return minTime
}

// Validacion Tema
const validateTema = (tema, info) => {
    if(!tema) return false;
    if(tema=="Otro"){
        let minLength = info.trim().length >= 3;
        let maxLength = info.trim().length <= 15;
        return minLength && maxLength;
    }
    return true;
};

// Validacion Fotos
const validateFiles = (files) => {
    if (!files) return false;
    let lengthValid = 1 <= files.length && files.length <= 5;
    let typeValid = true;
  
    for (const file of files) {
      // el tipo de archivo debe ser "image/<foo>" o "application/pdf"
      let fileFamily = file.type.split("/")[0];
      typeValid &&= fileFamily == "image" || file.type == "application/pdf";
    }
    return lengthValid && typeValid;
  };


// Validacion Formulario  
const validateForm = () => {
    let myForm = document.forms["myForm"];
    let region = myForm["select-region"];
    let comuna = myForm["select-comuna"];
    let sector = myForm["sector"];
    let nombre = myForm["nombre"];
    let email = myForm["email"];
    let tel = myForm["tel"];
    let contact = myForm["select-contact"];
    let info_contact = myForm["info-contact"];
    let inicio = myForm["inicio"];
    let termino = myForm["termino"];
    let tema = myForm["select-tema"];
    let infoTema = myForm["info-tema"];
    let input_files = myForm["files"];

    let isValid = true;
    // region
    if (!validateSelect(region.value)) {
        region.style.borderColor = "red";
        isValid = false;
    } else{
        region.style.borderColor = "";
    }
    // comuna
    if (!validateSelect(comuna.value)) {
        comuna.style.borderColor = "red";
        isValid = false;
    } else{
        comuna.style.borderColor = "";
    }
    // sector
    if (!validateSector(sector.value)) {
        sector.style.borderColor = "red";
        isValid = false;
    } else{
        sector.style.borderColor = "";
    }
    // nombre
    if (!validateName(nombre.value)) {
        nombre.style.borderColor = "red";
        isValid = false;
    } else{
       nombre.style.borderColor = "";
    }
    // email
    if (!validateEmail(email.value)) {
        email.style.borderColor = "red";
        isValid = false;
    } else{
        email.style.borderColor = "";
    }
    // telefono
    if (!validatePhoneNumber(tel.value)) {
        tel.style.borderColor = "red";
        isValid = false;
    } else{
        tel.style.borderColor = "";
    }
    // inicio
    if (!validateInitTime (inicio.value)) {
        inicio.style.borderColor = "red";
        isValid = false;
    } else{
        inicio.style.borderColor = "";
    }
    // termino
    if (!validateEndTime (inicio.value, termino.value)) {
        termino.style.borderColor = "red";
        isValid = false;
    } else{
        termino.style.borderColor = "";
    }
    // tema
    if (!validateTema (tema.value, infoTema.value)) {
        tema.style.borderColor = "red";
        infoTema.style.borderColor = "red";
        isValid = false;
    } else{
        tema.style.borderColor = "";
        infoTema.style.borderColor = "";
    }
    // termino
    if (!validateFiles (list_fotos)) {
        input_files.style.borderColor = "red";
        isValid = false;
    } else{
        input_files.style.borderColor = "";
    }
    

    let validationBox = document.getElementById("val-box");
    let validationMessageElem = document.getElementById("val-msg");
    let validationListElem = document.getElementById("val-list");
    let problemMessageElem = document.getElementById("problem-msg");
    let submitMessageElem = document.getElementById("submit-msg");

    if (!isValid){
        problemMessageElem.innerText = "Hay problemas con el formulario";
    }
    else{
        myForm.style.display = "none";
        submitBtn.style.display = "none";
        problemMessageElem.innerText = "";

        validationMessageElem.innerText = "¿Está seguro que desea agregar esta actividad?";
        validationListElem.textContent = "";

        // Agregar botones para enviar el formulario o volver
        let submitButton = document.createElement("button");
        submitButton.innerText = "Sí, estoy seguro";
        submitButton.className = "submit-btn";
        submitButton.style.marginRight = "10px";
        submitButton.addEventListener("click", () => {
            // crear formulario
            if (contact) contact.remove();
            if (info_contact) info_contact.remove();
            if (input_files) input_files.remove();

            const formData = new FormData(myForm);	// necesario ??

            // agregar manualmente contactos
            for (const contact in list_contacts) {
                list_contacts[contacts].forEach(i => {
	            formData.append(`contactos[${tipo}][]`, i)})
            }
            // agregar manualmente fotos
            for (const file of list_fotos) {
                formData.append("fotos[]", file);
            }
            // enviar formulario
            formData.submit();
            validationBox.style.display="none";
            submitMessageElem.innerText="Hemos recibido su información, muchas gracias y suerte en su actividad";
            // limpiar variables globales
            list_contacts = {};
            cnt_contacts = 0;
            list_fotos = [];
            cnt_fotos = 0;
        });

        let backButton = document.createElement("button");
        backButton.innerText = "No, no estoy seguro";
        backButton.className = "submit-btn";
        backButton.addEventListener("click", () => {
            // Mostrar el formulario nuevamente
            myForm.style.display = "block";
            submitBtn.style.display = "block";
            validationBox.hidden = true;
        });

        validationListElem.appendChild(submitButton);
        validationListElem.appendChild(backButton);

        // hacer visible el mensaje de validación
        validationBox.hidden = false;
    }
};


// Agregar informacion de contacto
let cnt_contacts = 0; 
let list_contacts = {}; 
const addContact = () => {
    let contact = document.getElementById("select-contact");
    let info = document.getElementById("info-contact");
    let infoText = document.getElementById("id-info");
    let errorMsg = document.getElementById("contact-error");
  
    if(cnt_contacts >= 5){
        errorMsg.innerText = "Solo puedes agregar hasta 5 contactos";
        return; 
    }
    else{
        if(contact.value==""){
            errorMsg.innerText = "Selecciona una opción de contacto";
        return; 
        }

        if(info.value==""){
            errorMsg.innerText = "Agrega un Id o Url para tu contacto";
            return; 
        }
    
        // agregar a la lista la info de contacto
        if(!list_contacts.hasOwnProperty(contact.value)) {
            list_contacts[contact.value] = [];
        }
        list_contacts[contact.value].push(info.value);
        errorMsg.innerText = "";
        cnt_contacts += 1;
        
        const entry = document.createElement("div");
        entry.className = "info-line";
        
        const span = document.createElement("span");
        span.innerText = `${info.value} (${contact.value})`;
        
        const removeBtn = document.createElement("button");
        removeBtn.innerText = "Eliminar";
        removeBtn.style.marginLeft = "10px";
        removeBtn.addEventListener("click", () => {
            infoText.removeChild(entry);
            // eliminar de la lista la info de contacto
            if (list_contacts[contact.value]) {
                list_contacts[contact.value] = list_contacts[contact.value].filter(i => i !== info.value)
                if(list_contacts[contact.value].length===0){
                    delete list_contacts[contact.value];
                }
            }

            cnt_contacts -= 1;
            if(cnt_contacts < 5){
            errorMsg.innerText = "";
            }
            
        });
        
        entry.appendChild(span);
        entry.appendChild(removeBtn);
        infoText.appendChild(entry);
        
        info.value = "";
    }
}

// Prellenar hora de termino
const setEndTime = () => {
    let inicio = document.getElementById("inicio")
    let termino = document.getElementById("termino")

    let startDate = new Date(inicio.value);
    const hours = startDate.getHours();
    startDate.setHours(hours - 1);  // tomar en cuenta las 4 hrs de diferencia con UTC

    termino.value = startDate.toISOString().slice(0, 16);
}

// Al seleccionar tema otros
const infoTema = () => {
    let tema = document.getElementById("select-tema");
    let info = document.getElementById("info-tema");
    if(tema.value == "Otro"){
        info.style.display = "block";
    }
    else{
        info.style.display = "none";
    }
}


// Agregar fotos
let cnt_fotos = 0;
let list_fotos = [];
const addPhoto = () => {
    let errorMsg = document.getElementById("files-error");
    let listMsg = document.getElementById("files-list");
    let file = document.getElementById("files");
    if(cnt_fotos <= 4){
        if(file && file.files.length > 0){
            cnt_fotos += 1;
            list_fotos.push(file.files[0]);
            errorMsg.innerText="";
            listMsg.innerText += `Se agregó la foto: ${file.value}\n`
        }
        else{
            errorMsg.innerText="Por favor seleccionar una foto";
        }
    }
    else{
        errorMsg.innerText="Se alcanzó el limite de fotos";
    }
}

// validar forms
let submitBtn = document.getElementById("btn-add-act");
submitBtn.addEventListener("click", validateForm);

// redireccionar pagina
let btnBack = document.getElementById("btn-back");
btnBack.addEventListener("click", redirectIndex);

// agregar informacion de contacto
let addInfoBtn = document.getElementById("add-info-btn");
addInfoBtn.addEventListener("click", addContact);

// setear hora de termino
let initTime = document.getElementById("inicio");
initTime.addEventListener("change", setEndTime);

// Opcion de agregar otro tema
let inputTema = document.getElementById("select-tema");
inputTema.addEventListener("change", infoTema);

// Agregar mas fotos
let addPhotoBtn = document.getElementById("add-photo-btn");
addPhotoBtn.addEventListener("click", addPhoto);

// resetear variables globales al cargar la página
window.addEventListener("DOMContentLoaded", () => {
    list_contacts = {};
    cnt_contacts = 0;
    list_fotos = [];
    cnt_fotos = 0;
    // myForm.reset();  // necesario ??
});
