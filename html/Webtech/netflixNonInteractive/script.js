

var button1 = document.getElementsByClassName("close");
var disp = document.getElementsByClassName("card2");
var c = 0;

function actionDrop(index) {
    if (c % 2 == 0) {
        button1[index].style.transform = "rotate(0)";
        disp[index].style.opacity = 1;
        disp[index].style.position = "relative";
        c=c+1;
    }
    else {
        button1[index].style.transform = "rotate(45deg)";
        disp[index].style.opacity = 0;
        disp[index].style.position = "absolute";
        c=c+1;
    }
}
