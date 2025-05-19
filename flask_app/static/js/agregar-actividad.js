
const redirectIndex = () => {
    window.location.href = "../home";
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
const validateFiles = (file, files_number) => {
    if (!file) return false;
    let lengthValid = 1 <= files_number && files_number <= 5;
    let typeValid = true;
    let fileFamily = file.type.split("/")[0];
    typeValid &&= fileFamily == "image" || file.type == "application/pdf";
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
    let inicio = myForm["inicio"];
    let termino = myForm["termino"];
    let tema = myForm["select-tema"];
    let infoTema = myForm["info-tema"];

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
    // fotos
    
    

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
        submitButton.setAttribute("type", "button"); 
        submitButton.innerText = "Sí, estoy seguro";
        submitButton.className = "submit-btn";
        submitButton.style.marginRight = "10px";
        submitButton.addEventListener("click", () => {
            // enviar formulario
            myForm.submit();
            //validationBox.style.display="none";
            //submitMessageElem.innerText="Hemos recibido su información, muchas gracias y suerte en su actividad";
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
const addContact = () => {
    let cnt_contacts = document.querySelectorAll('select[id^="select-contact"]').length;
    let contact = document.getElementById("select-contact"+cnt_contacts);
    let info = document.getElementById("info-contact"+cnt_contacts);
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
    
        createContactElem() // agregar el nuevo select e input
        errorMsg.innerText = "";
        return;
    }
}

const createContactElem = () => {
    let errorMsg = document.getElementById("contact-error");
    let cnt_contacts = document.querySelectorAll('select[id^="select-contact"]').length; 
    let cnt_contacts_n = cnt_contacts+1;

    const wrapper = document.createElement("div");
    wrapper.className = "contact-wrapper";

    // fila de select
    const selectRow = document.createElement("div");
    selectRow.className = "form-row";

    const originalSelect = document.getElementById("select-contact1");
    const select = originalSelect.cloneNode(true);
    select.name = "select-contact"+cnt_contacts_n;
    select.id = "select-contact"+cnt_contacts_n;
    select.selectedIndex = 0;
    select.style = "margin-left: 90px"

    selectRow.appendChild(select);

    // fila de input
    const inputRow = document.createElement("div");
    inputRow.className = "form-row";

    const originalInput = document.getElementById("info-contact1");
    const input = originalInput.cloneNode(true);
    input.name = "info-contact"+cnt_contacts_n;
    input.id = "info-contact"+cnt_contacts_n;
    input.value = "";
    input.style = "margin-left: 90px"

    inputRow.appendChild(input);

    // boton eliminar
    const deleteBtn = document.createElement("button");
    deleteBtn.type = "button";
    deleteBtn.className = "submit-btn-form";
    deleteBtn.innerText = "Eliminar";
    deleteBtn.style.marginLeft = "10px";
    deleteBtn.addEventListener("click", () => {
        errorMsg.innerText = "";
        wrapper.remove();
    });

    selectRow.appendChild(deleteBtn);

    wrapper.appendChild(selectRow);
    wrapper.appendChild(inputRow);

    const lastWrapper = document.querySelector(".contact-wrapper:last-of-type");

    if (lastWrapper) {
        lastWrapper.parentNode.insertBefore(wrapper, lastWrapper.nextSibling);
    } else {
        const baseInput = document.getElementById("info-contact1");
        const baseWrapper = baseInput.closest(".form-row").parentNode; 
        baseWrapper.parentNode.insertBefore(wrapper, baseWrapper.nextSibling);
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
const addPhoto = () => {
    let cnt_files = document.querySelectorAll('input[id^="file"]').length;
    let errorMsg = document.getElementById("files-error");
    let file = document.getElementById("file"+cnt_files);
    if(cnt_files <= 4){
        if(file && file.files.length > 0){
            createFileElem()
            errorMsg.innerText="";
            return;
        }
        else{
            errorMsg.innerText="Por favor seleccionar una foto";
            return;
        }
    }
    else{
        errorMsg.innerText="Se alcanzó el limite de fotos";
        return;
    }
}

const createFileElem = () => {
    let errorMsg = document.getElementById("files-error");
    let cnt_files = document.querySelectorAll('input[id^="file"]').length;
    let cnt_files_n = cnt_files+1;

    const wrapper = document.createElement("div");
    wrapper.className = "file-wrapper";

    const inputRow = document.createElement("div");
    inputRow.className = "form-row";

    const originalInput = document.getElementById("file1");
    const input = originalInput.cloneNode(true);
    input.name = "file"+cnt_files_n;
    input.id = "file"+cnt_files_n;
    input.value = "";
    input.style = "margin-left: 90px"

    inputRow.appendChild(input);

    // boton eliminar
    const deleteBtn = document.createElement("button");
    deleteBtn.type = "button";
    deleteBtn.className = "submit-btn-form";
    deleteBtn.innerText = "Eliminar";
    deleteBtn.style.marginLeft = "10px";
    deleteBtn.addEventListener("click", () => {
        errorMsg.innerText="";
        wrapper.remove();
    });

    inputRow.appendChild(deleteBtn);
    wrapper.appendChild(inputRow);

    const form = document.querySelector('form[name="myForm"]');
    const baseFileInput = document.getElementById("file1");
    const baseRow = baseFileInput.closest(".form-row");

    form.insertBefore(wrapper, errorMsg);
}

// validar forms
let submitBtn = document.getElementById("btn-add-act");
submitBtn.addEventListener("click", validateForm);

// redireccionar pagina
let btnBack = document.getElementById("btn-back");
btnBack.addEventListener("click", redirectIndex);

// agregar informacion de contacto
let addInfoBtn = document.getElementById("add-contact");
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

