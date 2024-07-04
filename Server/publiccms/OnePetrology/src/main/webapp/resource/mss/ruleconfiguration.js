function getnotificationMode() {
    var notificationMode = getSelectById("notificationMode");
    var email = document.getElementById("email");
    var phone = document.getElementById("phone");
    var page = document.getElementById("page");
    var emailText = document.getElementById("emailText");
    var phoneText = document.getElementById("phoneText");
    var pageText = document.getElementById("pageText");
    emailText.value="";
    phoneText.value="";
    pageText.value="";
    if (notificationMode == 1) {
       phone.style.display="none";
       page.style.display="none";
        email.style.display="inline-block";
    }

    if (notificationMode == 2) {
        email.style.display="none";
        page.style.display="none";
        phone.style.display="inline-block";
    }

    if (notificationMode == 3) {
        phone.style.display="none";
        email.style.display="none";
        page.style.display="inline-block";
    }

}

function rule() {
    var elements = getElements("ruleForm");
    var ruleName = elements[0];
    var ruleType = getSelectById("ruleType")
    var ruleCondition = getSelectById("ruleCondition")
    var conditionMax = elements[1];
    var calculation1 = getSelectById("calculation1")
    var conditionMin = elements[2];
    var calculation2 = getSelectById("calculation2")
    var priorityValue = elements[3];
    var notificationMode = getSelectById("notificationMode")
    var notificationModevalue = getnotificationModevalue()
    $.ajax({
        type:"POST",
        url:"http://localhost:8095/rule",
        data:{"ruleName":ruleName,"ruleType":ruleType,"ruleCondition":ruleCondition,"conditionMax":conditionMax,"calculation1":calculation1,"conditionMin":conditionMin,"calculation2":calculation2,"priorityValue":priorityValue,"notificationMode":notificationMode,"notificationModevalue":notificationModevalue},
        async:true,
        dataType:"json",
        success:function(data){

        },
        error:function(){

        },
        complete:function(){

        }
    });
}

function getnotificationModevalue() {
    var elements = getElements("ruleForm");
    var email = elements[4];
    var phone = elements[5];
    var page = elements[6];
    alert("email"+email)
    alert("phone"+phone)
    alert("page"+page)
    if (email != "" && email != null){
        return email;
    }if (phone != "" && phone != null){
        return phone;
    }if (page != "" && page != null){
        return page;
    }
}

function getElements(formId) {
    var form = document.getElementById(formId);
    var elements = new Array();
    var tagElements = form.getElementsByTagName('input');
    for (var j = 0; j < tagElements.length; j++){
        elements.push(tagElements[j].value);
    }
    return elements;
}

function getSelectById(selectId) {
    var selectId = document.getElementById(selectId);
    var selectedIndex = selectId.selectedIndex;
    var value = selectId.options[selectedIndex].value;
    return value;
}