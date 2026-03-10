// Modern Auth Helper Functions
// This ensures all auth pages work correctly

// Toggle Password Visibility
function togglePassword(inputId) {
    const input = document.getElementById(inputId);
    const icon = event.target;

    if (!input) return;

    if (input.type === 'password') {
        input.type = 'text';
        icon.classList.remove('fa-eye');
        icon.classList.add('fa-eye-slash');
    } else {
        input.type = 'password';
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
    }
}

// Show Toast Notification
function showToast(message, type = 'info') {
    const toast = document.getElementById('toast');
    if (!toast) return;

    toast.textContent = message;
    toast.className = 'toast show ' + type;

    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function () {
    console.log('Auth page helper initialized');
    initRecaptcha();
});

// Real-time Interactive reCAPTCHA Mock
function initRecaptcha() {
    const containers = document.querySelectorAll('.recaptcha-mock');
    if (containers.length === 0) return;

    containers.forEach((container, index) => {
        // Build unique IDs for each instance
        const triggerId = `rcTrigger_${index}`;
        const boxId = `rcBox_${index}`;

        container.innerHTML = `
            <div class="rc-left">
                <div class="rc-checkbox-wrapper" id="${triggerId}">
                    <div class="rc-checkbox" id="${boxId}"></div>
                </div>
                <span class="rc-text">I'm not a robot</span>
            </div>
            <div class="rc-right">
                <i class="fab fa-google"></i>
                <span>reCAPTCHA<br>Privacy - Terms</span>
            </div>
        `;

        const trigger = document.getElementById(triggerId);
        const box = document.getElementById(boxId);

        trigger.addEventListener('click', () => {
            if (container.dataset.verified === 'true') return;

            // 1. Start Spinning
            box.classList.add('loading');

            // 2. Simulate Verification Delay
            setTimeout(() => {
                box.classList.remove('loading');
                box.classList.add('verified');
                container.dataset.verified = 'true';
                console.log(`reCAPTCHA ${index} Verified`);

                // Set global flag if any is verified
                window._isRecaptchaVerified = true;
            }, 1200);
        });
    });
}
