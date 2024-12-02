document.addEventListener("DOMContentLoaded", () => {
    // Form validation for User Registration Form
    const registrationForm = document.querySelector("#user-registration-form");
    if (registrationForm) {
        registrationForm.addEventListener("submit", (event) => {
            const username = document.querySelector("#id_username");
            const email = document.querySelector("#id_email");
            const password1 = document.querySelector("#id_password1");
            const password2 = document.querySelector("#id_password2");

            let isValid = true;

            // Username validation
            if (!/^[a-zA-Z0-9_]+$/.test(username.value)) {
                isValid = false;
                alert("Username can only contain letters, numbers, and underscores.");
            }

            // Email validation
            if (!/^\S+@\S+\.\S+$/.test(email.value)) {
                isValid = false;
                alert("Please enter a valid email address.");
            }

            // Password validation
            if (password1.value !== password2.value) {
                isValid = false;
                alert("Passwords do not match.");
            }

            if (!isValid) event.preventDefault();
        });
    }

    // Form validation for Weather Search Form
    const weatherForm = document.querySelector("#weather-search-form");
    if (weatherForm) {
        weatherForm.addEventListener("submit", (event) => {
            const location = document.querySelector("#id_location");

            if (!/^[a-zA-Z\s]+$/.test(location.value)) {
                event.preventDefault();
                alert("Location must contain only letters and spaces.");
            }
        });
    }

    document.addEventListener("DOMContentLoaded", () => {
        const weatherForm = document.querySelector("#weather-search-form");

        if (weatherForm) {
            weatherForm.addEventListener("submit", (event) => {
                const location = document.querySelector("#id_location");
                const locationError = document.querySelector("#location-error");

                // Clear previous error message
                locationError.textContent = "";

                let isValid = true;

                // Validate location field
                if (!/^[a-zA-Z\s]+$/.test(location.value)) {
                    locationError.textContent = "Location must contain only letters and spaces.";
                    isValid = false;
                }

                // Prevent form submission if validation fails
                if (!isValid) {
                    event.preventDefault();
                }
            });
        }
    });

    document.addEventListener("DOMContentLoaded", () => {
        const loginForm = document.querySelector("#login-form");

        if (loginForm) {
            loginForm.addEventListener("submit", (event) => {
                let isValid = true;

                // Get form fields
                const username = document.querySelector("#id_username");
                const password = document.querySelector("#id_password");

                // Get error message elements
                const usernameError = document.querySelector("#username-error");
                const passwordError = document.querySelector("#password-error");

                // Clear previous error messages
                usernameError.textContent = "";
                passwordError.textContent = "";

                // Username validation
                if (username.value.trim() === "") {
                    usernameError.textContent = "Username cannot be empty.";
                    isValid = false;
                }

                // Password validation
                if (password.value.trim() === "") {
                    passwordError.textContent = "Password cannot be empty.";
                    isValid = false;
                }

                // Prevent form submission if validation fails
                if (!isValid) {
                    event.preventDefault();
                }
            });
        }
    });

});
