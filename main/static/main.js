var mybutton = document.getElementById("top"); // scroll to top button get

window.onscroll = function() { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) { // after 200 pixels btn shows
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

function topFunction() { // when clicked the button redirects to the top of the page
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}