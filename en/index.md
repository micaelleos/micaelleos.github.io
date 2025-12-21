---
layout: base
title: "Home Page"
lang: en
permalink: /en/
---

<header class="hero">
    <div class="container">
        <h1>{{ site.data.translations.home.hero.title.en }}</h1>
        <p>{{ site.data.translations.home.hero.subtitle.en }}</p>
        <a href="/en/portfolio" class="btn">{{ site.data.translations.buttons.explore_projects.en }}</a>
    </div>
</header>

<section id="about" class="about">
    <div class="container">
        <h2>{{ site.data.translations.home.about.title.en }}</h2>
        <div class="about-content">
            <div class="about-text">
                <p>{{ site.data.translations.home.about.bio_1.en }}</p>
                <p>{{ site.data.translations.home.about.bio_2.en }}</p>
            </div>
            <div class="about-image">
                <img src="/assets/img/PHOTO-2025-10-16-08-57-12-2.jpg" alt="My photo">
            </div>
        </div>
        <div class="social-buttons">
            <a href="{{ site.social.linkedin }}" target="_blank" class="social-btn linkedin">
                <i class="fab fa-linkedin"></i>
            </a>
            <a href="{{ site.social.github }}" target="_blank" class="social-btn github">
                <i class="fab fa-github"></i>
            </a>
            <a href="mailto:{{ site.author.email }}" class="social-btn email">
                <i class="fas fa-envelope"></i>
            </a>
        </div>
    </div>
</section>

<section id="specialties" class="specialties">
    <div class="container">
        <h2>{{ site.data.translations.home.specialties.title.en }}</h2>
        <div class="caixa"><p><i>{{ site.data.translations.home.specialties.subtitle.en }}</i></p></div>
        <div class="specialty-grid">
            <div class="specialty-item">
                <div class="specialty-icon">🧠</div>
                <h3>{{ site.data.translations.home.specialties.ai.title.en }}</h3>
                <p>{{ site.data.translations.home.specialties.ai.desc.en }}</p>
            </div>
            <div class="specialty-item">
                <div class="specialty-icon">🤖</div>
                <h3>{{ site.data.translations.home.specialties.agents.title.en }}</h3>
                <p>{{ site.data.translations.home.specialties.agents.desc.en }}</p>
            </div>
            <div class="specialty-item">
                <div class="specialty-icon">☁️</div>
                <h3>{{ site.data.translations.home.specialties.cloud.title.en }}</h3>
                <p>{{ site.data.translations.home.specialties.cloud.desc.en }}</p>
            </div>
            <div class="specialty-item">
                <div class="specialty-icon">🚀</div>
                <h3>{{ site.data.translations.home.specialties.prototyping.title.en }}</h3>
                <p>{{ site.data.translations.home.specialties.prototyping.desc.en }}</p>
            </div>
        </div>
    </div>
</section>

<section id="projects" class="projects">
    <div class="container">
        <h2>{{ site.data.translations.home.projects.title.en }}</h2>
        <div class="carousel">
            <button class="carousel-prev">❮</button>
            <div class="carousel-wrapper">
                <div class="project-grid"></div>
            </div>
            <button class="carousel-next">❯</button>
        </div>
    </div>
</section>

<section>
  <div class="container">
    <h2>{{ site.data.translations.home.blog.title.en }}</h2>
    <div class="posts2">
      {% for post in site.posts %}
        {% if post.lang == "en" %}
        <div class="post2">
          <h3><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h3>
          <p>{{ post.info }}</p>
          <a href="{{ post.url | prepend: site.baseurl }}" class="read-more">{{ site.data.translations.buttons.read_more.en }}</a>
        </div>
        {% endif %}
      {% endfor %}
    </div>
  </div>
</section>

<section id="badges" class="badges">
    <div class="container">
        <h2>{{ site.data.translations.home.badges.title.en }}</h2>
        <div class="badges-grid">
            <div class="badge-item">
                <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="08294967-be69-4efa-817f-af0ce1e2952c" data-share-badge-host="https://www.credly.com">
                </div>
                <script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
            </div>
            <div class="badge-item">
                <div class="badge-item" style=" border: 1px solid #e2e2e2; margin-top: -20px; padding: 35px 0px 0px 10px; border-radius: 0;">
                <a href="https://credentials.databricks.com/daa34c21-3a13-4dae-a680-062bf7aa5e49#acc.49E8fK5h" target="_blank">
                    <img src="https://api.accredible.com/v1/frontend/credential_website_embed_image/badge/133676259" alt="Databricks Badge" style="width:150px; height:270px;" class="databricks-badge-image">
                </a>
                    <p style = "margin-top:-120px">{{ site.data.translations.home.badges.academy_label.en }}</p>
                </div>
            </div>
            <div class="badge-item">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="5166bd3e-c455-4389-99fe-ed84ecfddae1" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
            </div>
            <div class="badge-item">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="7d132796-d481-41fb-b4ce-debb2c5af29d" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
            </div>
            <div class="badge-item">
                <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="e93bd35b-d0f7-4a5e-a5e5-1d49d0370185" data-share-badge-host="https://www.credly.com"></div>
                <script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
            </div>
            <div class="badge-item">
                <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="bf0e01c8-ee64-4a9d-90fe-3907ad80fc3d" data-share-badge-host="https://www.credly.com"></div>
                <script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
            </div>
        </div>
    </div>
</section>

<script>
    // JavaScript for animations and interactivity
    document.addEventListener('DOMContentLoaded', function() {
        // Smooth scrolling animation for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Entry animation for elements when they enter the viewport
        const animateOnScroll = (entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate');
                    observer.unobserve(entry.target);
                }
            });
        };

        const observer = new IntersectionObserver(animateOnScroll, {
            threshold: 0.1
        });

        document.querySelectorAll('.specialty-item, .project-item').forEach(item => {
            observer.observe(item);
        });

        // Contact form
        const contactForm = document.getElementById('contact-form');
        if (contactForm) {
            contactForm.addEventListener('submit', function(e) {
                e.preventDefault();
                alert('Thank you for contacting us! We will get back to you soon.');
                contactForm.reset();
            });
        }
    });

document.addEventListener('DOMContentLoaded', () => {
    async function loadProjects() {
        const currentLang = 'en';
        const projectFile = currentLang === 'pt' ? '/pt/projects.md' : '/en/projects.md';
        const response = await fetch(projectFile);
        const markdown = await response.text();
        const projects = parseMarkdown(markdown, currentLang);

        const projectGrid = document.querySelector('.project-grid');
        const prevButton = document.querySelector('.carousel-prev');
        const nextButton = document.querySelector('.carousel-next');

        // Render the projects
        projects.forEach(project => {
            const projectItem = document.createElement('div');
            projectItem.classList.add('project-item');

            projectItem.innerHTML = `
                <a href="${project.link}" target="_blank">
                <div class="project-image" style="background-image: url('${project.image}'); height: 150px; background-size: cover; border-radius: 8px;"></div>
                <h3>${project.name}</h3>
                <p>${project.description}</p>
                {{ site.data.translations.buttons.see_project.en }}</a>
            `;

            projectGrid.appendChild(projectItem);
        });

        // Carousel setup
        const projectWidth = projectGrid.children[0].offsetWidth + 20;
        const visibleProjects = window.innerWidth <= 768 ? 1 : 3;
        const totalProjects = projects.length;
        const maxIndex = Math.ceil(totalProjects / visibleProjects) - 1;
        let currentIndex = 0;

        const updateCarousel = () => {
            const offset = -(currentIndex * projectWidth * visibleProjects);
            projectGrid.style.transform = `translateX(${offset}px)`;
        };

        prevButton.addEventListener('click', () => {
            currentIndex = (currentIndex > 0) ? currentIndex - 1 : maxIndex;
            updateCarousel();
        });

        nextButton.addEventListener('click', () => {
            currentIndex = (currentIndex < maxIndex) ? currentIndex + 1 : 0;
            updateCarousel();
        });

        window.addEventListener('resize', () => {
            currentIndex = 0;
            updateCarousel();
        });
    }

    function parseMarkdown(markdown, lang) {
        const lines = markdown.split('\n');
        const projects = [];
        let currentProject = {};

        // Define prefixes based on language
        const prefixes = lang === 'pt'
            ? { description: 'Descrição: ', image: 'Imagem: ', link: 'Link: ' }
            : { description: 'Description: ', image: 'Image: ', link: 'Link: ' };

        lines.forEach(line => {
            if (line.startsWith('### ')) {
                if (Object.keys(currentProject).length) {
                    projects.push(currentProject);
                }
                currentProject = { name: line.replace('### ', '') };
            } else if (line.startsWith(prefixes.description)) {
                currentProject.description = line.replace(prefixes.description, '');
            } else if (line.startsWith(prefixes.image)) {
                currentProject.image = line.replace(prefixes.image, '');
            } else if (line.startsWith(prefixes.link)) {
                currentProject.link = line.replace(prefixes.link, '');
            }
        });

        if (Object.keys(currentProject).length) {
            projects.push(currentProject);
        }

        return projects;
    }

    loadProjects();
});
</script>
