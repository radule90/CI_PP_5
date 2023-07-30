// Header
// Collapsible Navbar
let menu = document.querySelector("#menu-bars");
let navbar = document.querySelector(".navbar");

menu.onclick = (event) => {
    event.preventDefault();
    menu.classList.toggle("fa-xmark");
    navbar.classList.toggle("active");
};

window.onscroll = () => {
    menu.classList.remove("fa-xmark");
    navbar.classList.remove("active");
};

// Search Form Overlay
document.querySelector("#search-icon").onclick = (event) => {
    event.preventDefault();
    document.querySelector("#search-form").classList.toggle("active");
    document.querySelector("#search-box").focus();
};

document.querySelector("#close").onclick = (event) => {
    event.preventDefault();
    document.querySelector("#search-form").classList.remove("active");
};

// Account Errors and Message Alert Disappear
let errorList = document.querySelectorAll('.errorlist');
let messages = document.querySelectorAll('.messages li');
if(errorList.length > 0) {
    errorList.forEach(error => setTimeout(() => {error.style.display = 'none'}, 3000));
};

if(messages.length > 0) {
    messages.forEach(message => setTimeout(() => {message.style.display = 'none'}, 3000));
}

// Footer
// Add Current Year In Footer Section
const year = document.querySelector("#year");
year.textContent = new Date().getFullYear();