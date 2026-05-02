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

// Header scroll effect
const header = document.querySelector('.site-header');
let lastScroll = 0;

window.addEventListener('scroll', () => {
  const currentScroll = window.pageYOffset;
  
  if (currentScroll > 100) {
    header.style.boxShadow = '0 2px 20px rgba(0,0,0,0.15)';
  } else {
    header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
  }
  
  lastScroll = currentScroll;
});

// Intersection Observer for fade-in animations
const observerOptions = {
  root: null,
  rootMargin: '0px',
  threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, observerOptions);

// Observe all cards and sections
document.querySelectorAll('.research-card, .collab-card, .section-header').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(20px)';
  el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  observer.observe(el);
});

// Active navigation highlighting
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.site-nav a[href^="#"]');

window.addEventListener('scroll', () => {
  let current = '';
  
  sections.forEach(section => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;
    
    if (pageYOffset >= sectionTop - 200) {
      current = section.getAttribute('id');
    }
  });
  
  navLinks.forEach(link => {
    link.style.color = '';
    if (link.getAttribute('href') === `#${current}`) {
      link.style.color = '#d69e2e';
    }
  });
});

// Form validation enhancement
const form = document.querySelector('.contact-form form');
if (form) {
  form.addEventListener('submit', (e) => {
    const button = form.querySelector('button[type="submit"]');
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
    button.disabled = true;
  });
}

// Mobile menu toggle (for future implementation)
const createMobileMenu = () => {
  const nav = document.querySelector('.site-nav');
  const header = document.querySelector('.header-content');
  
  if (window.innerWidth <= 768 && !document.querySelector('.mobile-menu-toggle')) {
    const toggle = document.createElement('button');
    toggle.className = 'mobile-menu-toggle';
    toggle.innerHTML = '<i class="fas fa-bars"></i>';
    toggle.style.cssText = `
      background: none;
      border: none;
      color: white;
      font-size: 1.5rem;
      cursor: pointer;
      display: block;
    `;
    
    toggle.addEventListener('click', () => {
      nav.style.display = nav.style.display === 'flex' ? 'none' : 'flex';
      if (nav.style.display === 'flex') {
        nav.style.cssText = `
          display: flex;
          flex-direction: column;
          position: absolute;
          top: 100%;
          left: 0;
          right: 0;
          background: #1a365d;
          padding: 1rem;
          box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        `;
      }
    });
    
    header.appendChild(toggle);
  }
};

window.addEventListener('resize', createMobileMenu);
createMobileMenu();

console.log('🎓 Dr. Antonio Alberti - Website loaded successfully');