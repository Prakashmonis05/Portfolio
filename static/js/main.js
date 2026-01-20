window.addEventListener('load', function() {
    const loadingScreen = document.getElementById('loading-screen');
    const progressFill = document.querySelector('.progress-fill');
    const percentage = document.querySelector('.percentage');
    
    let progress = 0;
    const interval = setInterval(() => {
        progress += Math.random() * 15;
        if (progress >= 100) {
            progress = 100;
            clearInterval(interval);
            setTimeout(() => {
                loadingScreen.classList.add('hidden');
                setTimeout(() => {
                    loadingScreen.style.display = 'none';
                }, 500);
            }, 300);
        }
        progressFill.style.width = progress + '%';
        percentage.textContent = Math.floor(progress) + '%';
    }, 100);
});

// Counter Animation
function animateCounter(element, target) {
    let current = 0;
    const increment = target / 100;
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        element.textContent = Math.floor(current) + '+';
    }, 20);
}

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.2,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            
            // Animate counters
            if (entry.target.classList.contains('stat-number')) {
                const target = parseInt(entry.target.getAttribute('data-target'));
                animateCounter(entry.target, target);
            }
        }
    });
}, observerOptions);

// Observe elements
document.addEventListener('DOMContentLoaded', function() {
    // Set initial state for animated elements
    const animatedElements = document.querySelectorAll('.project-card, .skill-category, .handle-card');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.6s ease';
        observer.observe(el);
    });
    
    // Observe stat numbers
    const statNumbers = document.querySelectorAll('.stat-number');
    statNumbers.forEach(stat => observer.observe(stat));
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// const menuToggle = document.getElementById('menu-toggle');
// const navMenu = document.getElementById('nav-menu');

// if (menuToggle && navMenu) {
//     menuToggle.addEventListener('click', function(e) {
//         e.preventDefault();
//         e.stopPropagation();
//         navMenu.classList.toggle('active');
//         console.log('Menu toggled:', navMenu.classList.contains('active'));
//     });

//     // Close menu when clicking on a link
//     const navLinks = navMenu.querySelectorAll('a');
//     navLinks.forEach(link => {
//         link.addEventListener('click', () => {
//             navMenu.classList.remove('active');
//         });
//     });

//     // Close menu when clicking outside
//     document.addEventListener('click', function(e) {
//         if (!navMenu.contains(e.target) && !menuToggle.contains(e.target)) {
//             navMenu.classList.remove('active');
//         }
//     });
// }

