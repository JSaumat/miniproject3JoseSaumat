document.addEventListener('DOMContentLoaded', function () {

    if (window.location.pathname === '/') {

        const modalElement = document.getElementById('ageModal');

        const modal = new bootstrap.Modal(modalElement, { keyboard: false });

        function setCookie(name, value, days) {

            let expires = "";

            if (days) {

                const date = new Date();

                date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));

                expires = "; expires=" + date.toUTCString();

            }

            document.cookie = name + "=" + value + expires + "; path=/";
        }

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

        if (!getCookie('ageVerified')) {

            modal.show(); // Show modal if cookie isn't set

        }

        document.getElementById('confirmAgeButton').addEventListener('click', function () {

            setCookie('ageVerified', 'true', 365 * 20); // Store cookie for 20 years

            modal.hide();

        });

        document.getElementById('denyAgeButton').addEventListener('click', function () {

            window.location.href = "https://www.google.com"; // Redirect if under 18

        });
    }
});
