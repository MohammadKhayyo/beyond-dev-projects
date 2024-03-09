document.getElementById("registrationForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission to view validation in action

    // Basic validation checks
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmPassword").value;
    var agreeToTerms = document.getElementById("agreeToTerms").checked;

    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return false;
    }

    if (!agreeToTerms) {
        alert("You must agree to the terms.");
        return false;
    }

    // If validation passes, here you would normally submit the form or do further processing
    alert("Form submitted successfully!");
});
