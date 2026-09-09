if ("scrollRestoration" in history) {
    history.scrollRestoration = "manual";
}

window.scrollTo(0, 0);

const sections = document.querySelectorAll(".animate-on-scroll");

function checkSections() {
    sections.forEach(function (section) {
        const sectionPosition = section.getBoundingClientRect().top;

        if (sectionPosition < window.innerHeight) {
            section.classList.add("show-animation");
        }
    });
}

window.addEventListener("scroll", checkSections);
checkSections();