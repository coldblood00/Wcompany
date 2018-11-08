function openNav(){
    document.getElementById("mySidenav").style.width="100%";
}
function closeNav(){
    document.getElementById("mySidenav").style.width="0px";

    document.body.style.backgroundColor="white";
}

window.onscroll=function(){scrollFunction()};
function scrollFunction(){
    if (document.body.scrollTop>20 || document.documentElement.scrollTop>20){
        document.getElementById("topBtn").style.display="block";
    }
    else{
        document.getElementById("topBtn").style.display="none";
    }
}

function topFunction(){
    document.body.scrollTop=0;
    document.documentElement.scrollTop=0;
}

function overMe(){
    document.getElementById("fingersup").style.animation="allbutton 1s ease infinite";
}

function outOfMe(){
    document.getElementById("fingersup").style.animation="allbutton 0s ease-in";
}

function onClick(){
    document.getElementById("html5").style.width="85%";
    document.getElementById("html5").style.color="white";
    document.getElementById("css").style.width="65%";
    document.getElementById("css").style.color="white";
    document.getElementById("javascript").style.width="32%";
    document.getElementById("javascript").style.color="white";
    document.getElementById("backend").style.width="30%";
    document.getElementById("backend").style.color="white";
    document.getElementById("skibut").style.fontSize="0";
    document.getElementById("skibut").style.borderColor="transparent";
}