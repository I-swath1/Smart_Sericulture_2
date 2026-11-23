
document.addEventListener("DOMContentLoaded", function () {

    const sections = document.querySelectorAll(".page-section");
    const navigationLinks = document.querySelectorAll("[data-page]");

    function showPage(pageName) {

        // Hide all pages
        sections.forEach(function (section) {
            section.classList.remove("active-page");
        });

        // Display only the selected page
        const selectedPage = document.getElementById(pageName);

        if (selectedPage) {
            selectedPage.classList.add("active-page");
        }

        // Highlight selected navigation item
        navigationLinks.forEach(function (link) {
            link.classList.toggle(
                "active",
                link.dataset.page === pageName
            );
        });

        // Update browser URL
        history.replaceState(null, "", "#" + pageName);

        // Return to the top
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    }

    // Handle navigation clicks
    navigationLinks.forEach(function (link) {

        link.addEventListener("click", function (event) {

            event.preventDefault();

            const pageName = this.dataset.page;

            showPage(pageName);

        });

    });

    // Open assessment automatically after image submission
    const initialPage = window.location.hash.replace("#", "");

    const validPages = [
        "home",
        "lifecycle",
        "assessment",
        "about"
    ];

    if (hasResults) {
        showPage("assessment");
    } else if (validPages.includes(initialPage)) {
        showPage(initialPage);
    } else {
        showPage("home");
    }

});

document.addEventListener("DOMContentLoaded", function () {

    // Read Flask result status from the body element
    const hasResults =
        document.body.dataset.hasResults === "true";

    const sections =
        document.querySelectorAll(".page-section");

    const navigationLinks =
        document.querySelectorAll("[data-page]");

    const validPages = [
        "home",
        "lifecycle",
        "assessment",
        "about"
    ];

    function showPage(pageName) {

        if (!validPages.includes(pageName)) {
            pageName = "home";
        }

        // Hide all pages
        sections.forEach(function (section) {
            section.classList.remove("active-page");
        });

        // Show selected page
        const selectedPage =
            document.getElementById(pageName);

        if (selectedPage) {
            selectedPage.classList.add("active-page");
        }

        // Highlight selected navigation item
        navigationLinks.forEach(function (link) {
            link.classList.toggle(
                "active",
                link.dataset.page === pageName
            );
        });

        // Update URL
        history.replaceState(null, "", "#" + pageName);

        // Scroll to top
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    }

    // Navigation click events
    navigationLinks.forEach(function (link) {

        link.addEventListener("click", function (event) {

            event.preventDefault();

            showPage(this.dataset.page);

        });

    });

    // Open assessment after form submission
    const initialPage =
        window.location.hash.replace("#", "");

    if (hasResults) {

        showPage("assessment");

    } else if (validPages.includes(initialPage)) {

        showPage(initialPage);

    } else {

        showPage("home");

    }

});
