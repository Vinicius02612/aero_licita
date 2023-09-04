let button_access_menu = document.querySelector(".open-menu");
let menu = document.querySelector(".menu");
window.addEventListener("scroll", () => {
    const scroll = window.scrollY;
    if (scroll > 0) {
        document.querySelector("header").classList.add("scroll");
    }
    else {
        document.querySelector("header").classList.remove("scroll");
    }
});

window.addEventListener("resize", () => {
    if (window.innerWidth > 848) {
        button_access_menu.style.display = "none";
        menu.classList.remove("active");
        menu.style.animation = "closeMenu 0.3s ease-in-out forwards";
        menu.style.display = "none";
        bars = button_access_menu.querySelectorAll(".bar");
        bars.forEach(bar => {
            bar.style.position = "relative";
        })
        bars[0].style.rotate = "0deg";
        bars[0].style.top = "0";

        bars[1].style.opacity = "1";

        bars[2].style.top = "0";
        bars[2].style.rotate = "0deg";
    }
    else {
        button_access_menu.style.display = "flex";
    }
});
button_access_menu.addEventListener("click", () => {
    if (menu.classList.contains("active")) {
        menu.classList.remove("active");
        menu.style.animation = "closeMenu 0.3s ease-in-out forwards";
        setTimeout(() => {
            menu.style.display = "none";
        }, 500);
        bars = button_access_menu.querySelectorAll(".bar");
        bars.forEach(bar => {
            bar.style.position = "relative";
        })
        bars[0].style.rotate = "0deg";
        bars[0].style.top = "0";

        bars[1].style.opacity = "1";

        bars[2].style.top = "0";
        bars[2].style.rotate = "0deg";
    }
    else {
        bars = button_access_menu.querySelectorAll(".bar");
        bars.forEach(bar => {
            bar.style.position = "absolute";
        })
        bars[0].style.rotate = "45deg";
        bars[0].style.top = "50%";

        bars[1].style.opacity = "0";

        bars[2].style.top = "50%";
        bars[2].style.rotate = "-45deg";

        menu.classList.add("active");
        menu.style.display = "flex";
        menu.style.animation = "openMenu 0.3s ease-in-out forwards";
    }
});
