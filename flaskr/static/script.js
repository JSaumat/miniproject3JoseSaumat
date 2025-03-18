document.addEventListener('DOMContentLoaded', function() {
    // Ensure the script runs ONLY on the home page (`/`)
    if (window.location.pathname === '/') {
        const modal = document.getElementById('ageModal');
        const confirmBtn = document.getElementById('confirmAgeButton');
        const denyBtn = document.getElementById('denyAgeButton');

        // Function to set a cookie
        function setCookie(name, value, days) {
            let expires = "";
            if (days) {
                const date = new Date();
                date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                expires = "; expires=" + date.toUTCString();
            }
            document.cookie = name + "=" + value + expires + "; path=/";
        }

        // Function to get a cookie value
        function getCookie(name) {
            const cookies = document.cookie.split('; ');
            for (let i = 0; i < cookies.length; i++) {
                const [cookieName, cookieValue] = cookies[i].split('=');
                if (cookieName === name) {
                    return cookieValue;
                }
            }
            return null;
        }

        // If the user has already confirmed their age, DO NOT show the modal
        if (getCookie('ageVerified')) {
            return; // Exit the function, do nothing
        }

        // If no cookie exists, show the modal on the home page
        if (modal) {
            modal.style.display = 'flex';
        }

        // When the user confirms they are 18+, set the cookie and hide the modal
        confirmBtn.addEventListener('click', function() {
            setCookie('ageVerified', 'true', 365 * 20); // Cookie lasts ~20 years
            modal.style.display = 'none'; // Hide the modal
        });

        // If the user clicks "I am not 18", redirect to Google
        denyBtn.addEventListener('click', function() {
            window.location.href = "https://www.google.com"; // Redirect to Google
        });
    }
});