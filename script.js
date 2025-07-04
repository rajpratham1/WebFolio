document.addEventListener('DOMContentLoaded', () => {
    // Mobile Navigation Toggle
    const navToggle = document.getElementById('navToggle');
    const navBarNav = document.getElementById('navbarNav');

    if (navToggle && navBarNav) {
        navToggle.addEventListener('click', () => {
            navBarNav.classList.toggle('active');
        });
    }

    // Smooth Scrolling for Navigation Links
    document.querySelectorAll('.nav-links a').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);

            if (targetSection) {
                const headerOffset = document.querySelector('.header').offsetHeight;
                const elementPosition = targetSection.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });

                if (navBarNav.classList.contains('active')) {
                    navBarNav.classList.remove('active');
                }
            }
        });
    });

    // Highlight active section in navigation on scroll
    const sections = document.querySelectorAll('section[id]');
    window.addEventListener('scroll', () => {
        let current = '';
        const headerHeight = document.querySelector('.header').offsetHeight;
        const scrollY = window.pageYOffset;

        sections.forEach(section => {
            const sectionTop = section.offsetTop - headerHeight - 10;
            const sectionHeight = section.clientHeight;
            if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });

        document.querySelectorAll('.nav-links a').forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').includes(current)) {
                link.classList.add('active');
            }
        });
    });

    // Set current year in footer
    const currentYearSpan = document.getElementById('currentYear');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }

    // --- Generic Form Submission Handler for Formspree ---
    async function handleFormspreeSubmission(event, statusElement, formElement) {
        event.preventDefault(); // Prevent default form submission

        statusElement.textContent = "Sending..."; // Show sending message
        statusElement.className = 'form-status'; // Reset classes
        statusElement.style.display = 'block'; // Make it visible

        const formData = new FormData(formElement);

        try {
            const response = await fetch(formElement.action, {
                method: formElement.method,
                body: formData,
                headers: {
                    'Accept': 'application/json' // Important for Formspree to return JSON
                }
            });

            if (response.ok) {
                statusElement.textContent = "Sent successfully!";
                statusElement.classList.add('success');
                formElement.reset(); // Clear the form fields
                
                // For quick inquiry forms, hide after success
                if (formElement.classList.contains('quick-inquiry-form')) {
                    setTimeout(() => {
                        formElement.classList.remove('active');
                        formElement.classList.add('hidden');
                        statusElement.style.display = 'none';
                    }, 3000); // Hide form and status after 3 seconds
                }
            } else {
                const data = await response.json();
                if (data.errors) {
                    // Try to extract specific error messages
                    const errorMessages = data.errors.map(err => err.message).join(", ");
                    statusElement.textContent = `Error: ${errorMessages}`;
                } else if (data.form) {
                    statusElement.textContent = `Error: ${data.form}`; // General form error
                } else {
                    statusElement.textContent = "Oops! There was an error sending your message.";
                }
                statusElement.classList.add('error');
            }
        } catch (error) {
            console.error('Submission error:', error);
            statusElement.textContent = "Network error. Please try again later.";
            statusElement.classList.add('error');
        }
    }

    // --- Attach event listener for the main detailed contact form ---
    const detailedContactForm = document.getElementById('detailedContactForm');
    const formStatusDetailed = document.getElementById('formStatusDetailed');

    if (detailedContactForm && formStatusDetailed) {
        detailedContactForm.addEventListener('submit', async function(e) {
            await handleFormspreeSubmission(e, formStatusDetailed, detailedContactForm);
        });
    }

    // --- Quick Inquiry Form Toggle and Submission ---
    const quickInquiryToggles = document.querySelectorAll('.quick-inquiry-toggle');

    quickInquiryToggles.forEach(button => {
        button.addEventListener('click', () => {
            const targetFormId = button.dataset.target;
            const targetForm = document.getElementById(targetFormId);

            // Hide any other active quick inquiry forms
            document.querySelectorAll('.quick-inquiry-form.active').forEach(form => {
                if (form.id !== targetFormId) {
                    form.classList.add('hidden');
                    form.classList.remove('active');
                    // Hide its status message if visible
                    const status = form.querySelector('.form-status');
                    if (status) status.style.display = 'none';
                    form.reset(); // Clear fields when hiding
                }
            });

            // Toggle the target form
            targetForm.classList.toggle('hidden');
            targetForm.classList.toggle('active');

            // Hide its status message when toggling
            const status = targetForm.querySelector('.form-status');
            if (status) status.style.display = 'none';

            // Reset the form fields when it becomes visible (or toggled)
            if (targetForm.classList.contains('active')) {
                targetForm.reset();
            }
        });
    });

    // Attach submit event listeners to each quick inquiry form
    document.querySelectorAll('.quick-inquiry-form').forEach(form => {
        const statusElement = form.querySelector('.form-status');
        if (statusElement) {
            form.addEventListener('submit', async function(e) {
                await handleFormspreeSubmission(e, statusElement, form);
            });
        }
    });
});