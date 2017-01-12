/**
 * Created by laurajuvancic on 10/11/16.
 */

function showFormList() {
    document.getElementById('formlist').style.display = "block";
    document.getElementById('formtext').style.display = "block";
}

function hideFormList() {
    document.getElementById('formlist').style.display = "none";
    document.getElementById('formtext').style.display = "none";
    document.getElementById('formhome').style.display = "none";
    document.getElementById('formwork').style.display = "none";
    document.getElementById('formpersonal').style.display = "none";
    document.getElementById('formtravel').style.display = "none";
    document.getElementById('formshopping').style.display = "none";
    document.getElementById('formbirthday').style.display = "none";
    document.getElementById('formcooking').style.display = "none";
    document.getElementById('formcookinglist').style.display = "none";
    document.getElementById('task1').style.display = "none";
    document.getElementById('task2').style.display = "none";
}

function hidetasks() {
    document.getElementById('task1').style.display = "none";
    document.getElementById('task2').style.display = "none";
    document.getElementById('formcookinglist').style.display = "none";
}

function showForm(element) {
    switch (element.value){
        case 'select':
            document.getElementById('formhome').style.display = "none";
            document.getElementById('formwork').style.display = "none";
            document.getElementById('formpersonal').style.display = "none";
            document.getElementById('formtravel').style.display = "none";
            document.getElementById('formshopping').style.display = "none";
            document.getElementById('formbirthday').style.display = "none";
            document.getElementById('formcooking').style.display = "none";
            document.getElementById('formcookinglist').style.display = "none";
            break;
        case 'home':
            document.getElementById('formhome').style.display = "block";
            document.getElementById('formwork').style.display = "none";
            document.getElementById('formpersonal').style.display = "none";
            document.getElementById('formtravel').style.display = "none";
            document.getElementById('formshopping').style.display = "none";
            document.getElementById('formbirthday').style.display = "none";
            document.getElementById('formcooking').style.display = "none";
            document.getElementById('formcookinglist').style.display = "none";
            break;
        case 'work':
            document.getElementById('formwork').style.display = "block";
            document.getElementById('formhome').style.display = "none";
            document.getElementById('formpersonal').style.display = "none";
            document.getElementById('formtravel').style.display = "none";
            document.getElementById('formshopping').style.display = "none";
            document.getElementById('formbirthday').style.display = "none";
            document.getElementById('formcooking').style.display = "none";
            document.getElementById('formcookinglist').style.display = "none";
            break;
        case 'personal':
            document.getElementById('formpersonal').style.display = "block";
            document.getElementById('formhome').style.display = "none";
            document.getElementById('formwork').style.display = "none";
            document.getElementById('formtravel').style.display = "none";
            document.getElementById('formshopping').style.display = "none";
            document.getElementById('formbirthday').style.display = "none";
            document.getElementById('formcooking').style.display = "none";
            document.getElementById('formcookinglist').style.display = "none";
            break;
        case 'travel':
            document.getElementById('formtravel').style.display = "block";
            document.getElementById('formhome').style.display = "none";
            document.getElementById('formwork').style.display = "none";
            document.getElementById('formpersonal').style.display = "none";
            document.getElementById('formshopping').style.display = "none";
            document.getElementById('formbirthday').style.display = "none";
            document.getElementById('formcooking').style.display = "none";
            document.getElementById('formcookinglist').style.display = "none";
            break;
        case 'shopping':
            document.getElementById('formshopping').style.display = "block";
            document.getElementById('formhome').style.display = "none";
            document.getElementById('formwork').style.display = "none";
            document.getElementById('formpersonal').style.display = "none";
            document.getElementById('formtravel').style.display = "none";
            document.getElementById('formbirthday').style.display = "none";
            document.getElementById('formcooking').style.display = "none";
            document.getElementById('formcookinglist').style.display = "none";
            break;
        case 'birthday':
            document.getElementById('formbirthday').style.display = "block";
            document.getElementById('formhome').style.display = "none";
            document.getElementById('formwork').style.display = "none";
            document.getElementById('formpersonal').style.display = "none";
            document.getElementById('formtravel').style.display = "none";
            document.getElementById('formshopping').style.display = "none";
            document.getElementById('formcooking').style.display = "none";
            document.getElementById('formcookinglist').style.display = "none";
            break;
        case 'cooking':
            document.getElementById('formcooking').style.display = "block";
            document.getElementById('formcookinglist').style.display = "block";
            document.getElementById('formhome').style.display = "none";
            document.getElementById('formwork').style.display = "none";
            document.getElementById('formpersonal').style.display = "none";
            document.getElementById('formtravel').style.display = "none";
            document.getElementById('formshopping').style.display = "none";
            document.getElementById('formbirthday').style.display = "none";
            break;
    }

}

function showlogin(element) {
    if(document.getElementById('login').style.display == "block") {
        document.getElementById('login').style.display = "none";
        document.getElementById('loginlist').style.display = "none";
    }
    else {
        document.getElementById('login').style.display = "block";
        document.getElementById('loginlist').style.display = "block";
    }
    return false;
}

function showUser(element) {
    if(document.getElementById('user').style.display == "block") {
        document.getElementById('user').style.display = "none";
        document.getElementById('userlist').style.display = "none";
    }
    else {
        document.getElementById('user').style.display = "block";
        document.getElementById('userlist').style.display = "block";
    }

    return false;
}

function focus1(element){
    document.getElementById('dim').style.display = "block";
    document.getElementById('focus1').style.display = "block";

    return false;
}

function hidefocus1() {
    document.getElementById('dim').style.display = "none";
    document.getElementById('focus1').style.display = "none";
}

function focus2(element){
    document.getElementById('dim').style.display = "block";
    document.getElementById('focus2').style.display = "block";

    return false;
}

function hidefocus2() {
    document.getElementById('dim').style.display = "none";
    document.getElementById('focus2').style.display = "none";
}

function focus3(element){
    document.getElementById('dim').style.display = "block";
    document.getElementById('focus3').style.display = "block";

    return false;
}

function hidefocus3() {
    document.getElementById('dim').style.display = "none";
    document.getElementById('focus3').style.display = "none";
}

function focus4(element){
    document.getElementById('dim').style.display = "block";
    document.getElementById('focus4').style.display = "block";

    return false;
}

function hidefocus4() {
    document.getElementById('dim').style.display = "none";
    document.getElementById('focus4').style.display = "none";
}

function focus5(element){
    document.getElementById('dim').style.display = "block";
    document.getElementById('focus5').style.display = "block";

    return false;
}

function hidefocus5() {
    document.getElementById('dim').style.display = "none";
    document.getElementById('focus5').style.display = "none";
}

function focus6(element){
    document.getElementById('dim').style.display = "block";
    document.getElementById('focus6').style.display = "block";

    return false;
}

function hidefocus6() {
    document.getElementById('dim').style.display = "none";
    document.getElementById('focus6').style.display = "none";
}

function focus7(element){
    document.getElementById('dim').style.display = "block";
    document.getElementById('focus7').style.display = "block";

    return false;
}

function hidefocus7() {
    document.getElementById('dim').style.display = "none";
    document.getElementById('focus7').style.display = "none";
}


function showNotifications(element) {
    if(document.getElementById('notifications').style.display == "block") {
        document.getElementById('notifications').style.display = "none";
    }
    else {
        document.getElementById('notifications').style.display = "block";
    }

    return false;
}
