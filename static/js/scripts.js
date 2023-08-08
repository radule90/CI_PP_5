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
const errorList = document.querySelectorAll('.errorlist');
if (errorList.length > 0) {
    errorList.forEach(error => {
        setTimeout(() => {
            error.style.opacity = 0;
            setTimeout(() => { error.style.display = 'none'; }, 2000);
        }, 2000);
    });
}

// Django Alert Messages
// Logic for message fade out and for close button
document.addEventListener("DOMContentLoaded", function () {
    const messageWrapper = document.querySelectorAll('.messages-wrapper');
    if (messageWrapper.length > 0) {
        messageWrapper.forEach(message => {
            setTimeout(() => {
                message.style.opacity = 0;
                setTimeout(() => {
                    message.style.display = 'none';
                }, 2000);
            }, 2000);
        });
    }

    const closeButtons = document.querySelectorAll(".close-message");
    closeButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const messageItem = button.closest("li");
            if (messageItem) {
                messageItem.remove();
            }
        });
    });
});

// Dashboard Collapsable Menu
document.addEventListener('DOMContentLoaded', function() {
    const dashboard = document.querySelector("#dashboard-nav-icon");
    const dashboardNav = document.querySelector(".dashboard-list");

    if (dashboard) {
        dashboard.addEventListener('mouseover', () => {
            dashboard.classList.toggle("fa-bounce");
        });

        dashboard.addEventListener('mouseout', () => {
            dashboard.classList.toggle("fa-bounce");
        });

        dashboard.onclick = (event) => {
            event.preventDefault();
            dashboardNav.classList.toggle("active");
        };
    }
});

// Shop Filter Collapsable Menu
document.addEventListener('DOMContentLoaded', function() {
    const filterIcon = document.querySelector("#filter-nav-icon");
    const filterGroup = document.querySelector(".filter-group");

    if (filterIcon) {
        filterIcon.addEventListener('mouseover', () => {
            filterIcon.classList.toggle("fa-bounce");
        });

        filterIcon.addEventListener('mouseout', () => {
            filterIcon.classList.toggle("fa-bounce");
        });

        filterIcon.onclick = (event) => {
            event.preventDefault();
            filterGroup.classList.toggle("active");
        };
    }
});

// Footer
// Add Current Year In Footer Section
const year = document.querySelector("#year");
year.textContent = new Date().getFullYear();