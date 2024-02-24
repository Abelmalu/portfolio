const toggleButton = document.getElementsByClassName("toggle-button")[0];
const navbarLinks = document.getElementsByClassName("navbar-links")[0];

toggleButton.addEventListener("click", () => {
  navbarLinks.classList.toggle("active");
});


const themeToggler = document.querySelector('.theme-toggler');


var icon = document.getElementById("icon")
var light = document.getElementById("light")

icon.onclick = function () {

    // document.body.classList.toggle("dark")
    document.body.style.backgroundColor = '#0E1428'
  
    // if (document.body.classList.contains("dark")) {
        light.style.display = 'inline'
        icon.style.display = 'none'
        
        
    // }
    
    }


light.onclick = function () {
    // document.body.classList.toggle("sun")
    document.body.style.backgroundColor='#41292C'


    // if (document.body.classList.contains("sun")) {
        
        icon.style.display = 'inline'
        light.style.display = 'none'
    // }
    
}