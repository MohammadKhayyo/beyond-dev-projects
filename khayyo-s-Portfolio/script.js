// script.js
document.addEventListener('DOMContentLoaded', function () {
    const contactForm = document.getElementById('contact-form');

    contactForm.addEventListener('submit', function (event) {
        // Prevent the default form submission
        event.preventDefault();

        // Simple form validation feedback
        const name = contactForm.querySelector('input[name="name"]').value.trim();
        const email = contactForm.querySelector('input[name="email"]').value.trim();
        const message = contactForm.querySelector('textarea[name="message"]').value.trim();

        if (name && email && message) {
            console.log('Name:', name);
            console.log('Email:', email);
            console.log('Message:', message);
            alert('Thank you for your message, ' + name + '!');
            // Here you would normally send the form data to the server
            // Reset the form after submission
            contactForm.reset();
        } else {
            alert('Please fill in all fields.');
        }
    });
});
