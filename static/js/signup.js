var name1 = document.getElementById("name1");
var name2 = document.getElementById("name2");
var email = document.getElementById("email");
var pass1 = document.getElementById("pass1");
var pass2 = document.getElementById("pass2");


function validname1(){
    var fn = name1.value
    if (isNaN(fn)) {
        name1.className = "success";
        document.getElementById("text").innerHTML = "";
    } else {
        name1.className = "error";
        document.getElementById("signup").disabled = true;
        document.getElementById("text").innerHTML = "please enter Firstname";
    }
}

function validname2(){
    var fn = name2.value
    if (isNaN(fn)) {
        name2.className = "success";
        document.getElementById("text").innerHTML = "";
    } else {
        name2.className = "error";
        document.getElementById("signup").disabled = true;
        document.getElementById("text").innerHTML = "please enter  Lastname";
    }
}

function validemail() {
    var mail = email.value;
    var re = /^[a-zA-Z0-9.!#$%&'+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$/;
    if (re.test(mail)) {
        email.className = "success";
        document.getElementById("text").innerHTML = "";
    } else {
        email.className = "error";
        document.getElementById("signup").disabled = true;
        document.getElementById("text").innerHTML = "please enter the valid email";

    }
}



function validph() {
    var num = ph.value;
    if (isNaN(num)) {
        ph.className = "error";
        document.getElementById("signup").disabled = true;
        document.getElementById("text").innerHTML = "please enter the valid phone number";
    } else {
        var numl = num.length;
        if (numl == 10) {
            ph.className = "success";
            document.getElementById("text").innerHTML = "";
        } else {
            ph.className = "error";
            document.getElementById("signup").disabled = true;
            document.getElementById("text").innerHTML = "please enter the valid phone number";
        }
    }
}


    function validpass() {
        var passl = pass1.value.length;
        if (passl >= 8 & passl <= 16) {
            pass1.className = "success";
            document.getElementById("text").innerHTML = "";
        } else {
            pass1.className = "error";
            document.getElementById("signup").disabled = true;
            document.getElementById("text").innerHTML = "Password length must be greater than 8 characters.and not excced 15 ";
        }
    }

    function validpassconform() {
        var pass = pass1.value;
        var passc = pass2.value;
        if (pass == passc) {
            pass2.className = "success";
            document.getElementById("text").innerHTML = "";
            document.getElementById("signup").disabled = false;
        
        } else {
            document.getElementById("signup").disabled = true;
            pass2.className = "error";
            document.getElementById("text").innerHTML = "Password not match";
        }
    }

document.getElementById("signup").disabled = true;

