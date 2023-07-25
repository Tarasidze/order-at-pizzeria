document.addEventListener('DOMContentLoaded', () => {
  const loginFormContainer = document.querySelector('.login-form-container');

  // Animate the login form container when the page is loaded
  loginFormContainer.style.opacity = '0';
  setTimeout(() => {
    loginFormContainer.style.transition = 'opacity 1s ease';
    loginFormContainer.style.opacity = '1';
  }, 100);
});
