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
