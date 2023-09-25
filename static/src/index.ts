import './js/alpine'
import './js/gsap/gsap.min'
import './main.scss'

let lastScroll = 0;
const nav = document.getElementById("navbar-sticky") as HTMLElement;
console.log(document.querySelector("#hero-space"));


window.addEventListener("scroll", () => {
    const currentScroll = window.scrollY;

    if (currentScroll < 0) {
        nav.classList.remove("show");
    }
    if (currentScroll > lastScroll && !nav.classList.contains("hide")) {
        nav.classList.remove("show");
        nav.classList.add("hide");
    }
    if (currentScroll < lastScroll && nav.classList.contains("hide")) {
        nav.classList.remove("hide");
        nav.classList.add("show");
    }
    if (currentScroll > 200) {
        nav.classList.add("bg-white");
    } else {
        nav.classList.remove("bg-white");
    }
    lastScroll = currentScroll;
});