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

const togglePasswordIcons = document.querySelectorAll('.toggle-password');
togglePasswordIcons.forEach(icon => {
    icon.addEventListener('click', function () {
        const inputField = this.previousElementSibling;

        if (inputField && inputField.tagName === 'INPUT') {
            const type = inputField.getAttribute('type') === 'password' ? 'text' : 'password';
            inputField.setAttribute('type', type);

            if (type === 'password') {
                this.classList.remove('bx-show');
                this.classList.add('bx-hide');
            } else {
                this.classList.remove('bx-hide');
                this.classList.add('bx-show');
            }
        }
    });
});

const API_BASE_URL = ['localhost', '127.0.0.1', '[::1]', '::1', '[::]', '::'].includes(window.location.hostname)
    ? 'http://127.0.0.1:8000'
    : window.location.origin;

const loginForm = document.getElementById('login-form');
if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const username = document.getElementById('login-username').value;
        const passwordInput = document.getElementById('login-password').value;
        const loginBtn = loginForm.querySelector('.login-btn');
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
                window.location.href = '/home%20page/home_page.html';
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

const registerForm = document.getElementById('register-form');
if (registerForm) {
    registerForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const password = document.getElementById('reg-password').value;
        const confirmPassword = document.getElementById('reg-confirm-password').value;

        if (password !== confirmPassword) {
            alert("Passwords do not match");
            return;
        }

        const regBtn = registerForm.querySelector('.register-btn');
        const originalBtnText = regBtn.textContent;
        regBtn.textContent = 'Registering...';
        regBtn.disabled = true;

        const data = {
            employee_id: document.getElementById('reg-employee-id').value,
            full_name: document.getElementById('reg-full-name').value,
            email: document.getElementById('reg-email').value,
            department: document.getElementById('reg-department').value,
            role: document.getElementById('reg-role').value,
            manager_id: document.getElementById('reg-manager-id').value,
            password: password
        };

        try {
            const response = await fetch(`${API_BASE_URL}/register`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                alert('Registration successful! Please login.');
                document.querySelector('.container').classList.remove('active');
                registerForm.reset();
            } else {
                const errorData = await response.json();
                alert(errorData.detail || 'Registration failed.');
            }
        } catch (error) {
            console.error('Registration error:', error);
            alert('Failed to connect to the authentication server.');
        } finally {
            regBtn.textContent = originalBtnText;
            regBtn.disabled = false;
        }
    });
}

