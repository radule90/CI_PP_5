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
};
document.querySelector("#close").onclick = (event) => {
    event.preventDefault();
    document.querySelector("#search-form").classList.remove("active");
};

// Footer
// Add Current Year In Footer Section
const year = document.querySelector("#year");
year.textContent = new Date().getFullYear();