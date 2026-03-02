const container = document.querySelector('.container');
const registerBtn = document.querySelector('.register-button');
const loginBtn = document.querySelector('.login-button');

registerBtn.addEventListener('click', () => {
    container.classList.add('active');
});

loginBtn.addEventListener('click', () => {
    container.classList.remove('active');
});

const passwordInputs = document.querySelectorAll('.form-box.register input[type="password"]');
if (passwordInputs.length >= 2) {
    const password = passwordInputs[0];
    const confirmPassword = passwordInputs[1];

    function validatePassword() {
        if (password.value !== confirmPassword.value) {
            confirmPassword.setCustomValidity("Passwords do not match");
        } else {
            confirmPassword.setCustomValidity('');
        }
    }

    password.addEventListener('change', validatePassword);
    confirmPassword.addEventListener('keyup', validatePassword);
}

// API Configuration
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://localhost:8000'
    : window.location.origin;

// Login Form Handling
const loginForm = document.getElementById('login-form');
if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const username = document.getElementById('login-username').value;
        const passwordInput = document.getElementById('login-password').value;
        const loginBtn = loginForm.querySelector('.login-btn');

        // Show loading state
        const originalBtnText = loginBtn.textContent;
        loginBtn.textContent = 'Logging in...';
        loginBtn.disabled = true;

        try {
            const formData = new URLSearchParams();
            formData.append('username', username);
            formData.append('password', passwordInput);

            const response = await fetch(`${API_BASE_URL}/login`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: formData
            });

            if (response.ok) {
                const data = await response.json();
                localStorage.setItem('access_token', data.access_token);
                // Redirect to homepage
                window.location.href = '../home page/home_page.html';
            } else {
                const errorData = await response.json();
                alert(errorData.detail || 'Invalid username or password.');
            }
        } catch (error) {
            console.error('Login error:', error);
            alert('Failed to connect to the authentication server.');
        } finally {
            loginBtn.textContent = originalBtnText;
            loginBtn.disabled = false;
        }
    });
}
