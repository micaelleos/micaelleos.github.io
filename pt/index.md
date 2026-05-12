---
layout: base
title: "Página Inicial"
lang: pt
permalink: /pt/
---

<header class="hero">
    <div class="container">
        <h1>{{ site.data.translations.home.hero.title.pt }}</h1>
        <p>{{ site.data.translations.home.hero.subtitle.pt }}</p>
        <a href="/pt/portfolio" class="btn">{{ site.data.translations.buttons.explore_projects.pt }}</a>
    </div>
</header>

<section id="about" class="about">
    <div class="container">
        <h2>{{ site.data.translations.home.about.title.pt }}</h2>
        <div class="about-content">
            <div class="about-text">
                <p>{{ site.data.translations.home.about.bio_1.pt }}</p>
                <p>{{ site.data.translations.home.about.bio_2.pt }}</p>
            </div>
            <div class="about-image">
                <img src="/assets/img/PHOTO-2025-10-16-08-57-12-2.jpg" alt="Minha foto">
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
        <h2>{{ site.data.translations.home.specialties.title.pt }}</h2>
        <div class="caixa"><p><i>{{ site.data.translations.home.specialties.subtitle.pt }}</i></p></div>
        <div class="specialty-grid">
            <div class="specialty-item">
                <div class="specialty-icon">🧠</div>
                <h3>{{ site.data.translations.home.specialties.ai.title.pt }}</h3>
                <p>{{ site.data.translations.home.specialties.ai.desc.pt }}</p>
            </div>
            <div class="specialty-item">
                <div class="specialty-icon">🤖</div>
                <h3>{{ site.data.translations.home.specialties.agents.title.pt }}</h3>
                <p>{{ site.data.translations.home.specialties.agents.desc.pt }}</p>
            </div>
            <div class="specialty-item">
                <div class="specialty-icon">🚀</div>
                <h3>{{ site.data.translations.home.specialties.prototyping.title.pt }}</h3>
                <p>{{ site.data.translations.home.specialties.prototyping.desc.pt }}</p>
            </div>
            <div class="specialty-item">
                <div class="specialty-icon">🏗️</div>
                <h3>{{ site.data.translations.home.specialties.cloud_arch.title.pt }}</h3>
                <p>{{ site.data.translations.home.specialties.cloud_arch.desc.pt }}</p>
            </div>
        </div>
    </div>
</section>

<section id="projects" class="projects">
    <div class="container">
        <h2>{{ site.data.translations.home.projects.title.pt }}</h2>
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
    <h2>{{ site.data.translations.home.blog.title.pt }}</h2>
    <div class="posts2">
      {% for post in site.posts %}
        {% if post.lang == "pt" %}
        <div class="post2">
          <h3><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h3>
          <p>{{ post.info }}</p>
          <a href="{{ post.url | prepend: site.baseurl }}" class="read-more">{{ site.data.translations.buttons.read_more.pt }}</a>
        </div>
        {% endif %}
      {% endfor %}
    </div>
  </div>
</section>

<section id="badges" class="badges">
    <div class="container">
        <h2>{{ site.data.translations.home.badges.title.pt }}</h2>
        <div class="carousel badges-carousel">
            <button class="carousel-prev badges-prev">❮</button>
            <div class="carousel-wrapper">
            <div class="badges-track">
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
                    <p style = "margin-top:-120px">{{ site.data.translations.home.badges.academy_label.pt }}</p>
                </div>
            </div>
            <div class="badge-item">
                <div style="text-align: center; border: 1px solid #e2e2e2; padding: 25px 10px 0px 10px; border-radius: 0; margin-top: -15px;">
                <a href="https://credentials.databricks.com/0458f56b-a0f4-4276-b6a6-8caa7b096f0f#acc.Nqns7Bg0" target="_blank">
                    <img src="https://www.databricks.com/sites/default/files/2025-10/Associate-badge-ML.png?v=1761077024" alt="Databricks ML Engineer Badge" style="max-width:105px; height:auto; display:block; margin:0 auto;">
                </a>
                    <p style="margin-top: 8px; font-size: 0.8rem;">{{ site.data.translations.home.badges.ml_engineer_label.pt }}</p>
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
            <button class="carousel-next badges-next">❯</button>
        </div>
    </div>
</section>

<script>
    // JavaScript para animações e interatividade
    document.addEventListener('DOMContentLoaded', function() {
        // Animação de rolagem suave para links de navegação
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Animação de entrada para elementos quando entram no viewport
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

        // Formulário de contato
        const contactForm = document.getElementById('contact-form');
        if (contactForm) {
            contactForm.addEventListener('submit', function(e) {
                e.preventDefault();
                alert('Obrigado por entrar em contato! Retornaremos em breve.');
                contactForm.reset();
            });
        }
    });

document.addEventListener('DOMContentLoaded', () => {
    async function loadProjects() {
        const currentLang = 'pt';
        const projectFile = currentLang === 'pt' ? '/pt/projects.md' : '/en/projects.md';
        const response = await fetch(projectFile);
        const markdown = await response.text();
        const projects = parseMarkdown(markdown, currentLang);

        const projectGrid = document.querySelector('.project-grid');
        const prevButton = document.querySelector('.carousel-prev');
        const nextButton = document.querySelector('.carousel-next');

        // Renderizar projetos
        projects.forEach(project => {
            const projectItem = document.createElement('div');
            projectItem.classList.add('project-item');

            projectItem.innerHTML = `
                <a href="${project.link}" target="_blank">
                <div class="project-image" style="background-image: url('${project.image}'); height: 150px; background-size: cover; background-position: center 50%; border-radius: 8px;"></div>
                <h3>${project.name}</h3>
                <p>${project.description}</p>
                {{ site.data.translations.buttons.see_project.pt }}</a>
            `;

            projectGrid.appendChild(projectItem);
        });

        // Configuração do carousel
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

        // Define os prefixos baseados no idioma
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

document.addEventListener('DOMContentLoaded', () => {
    const badgesTrack = document.querySelector('.badges-track');
    const badgesPrev = document.querySelector('.badges-prev');
    const badgesNext = document.querySelector('.badges-next');
    const badgesWrapper = document.querySelector('.badges-carousel .carousel-wrapper');

    if (!badgesTrack || !badgesWrapper) return;

    const gap = 20;
    let visibleBadges = window.innerWidth <= 768 ? 2 : 5;
    const totalBadges = badgesTrack.children.length;
    let maxIndex = Math.ceil(totalBadges / visibleBadges) - 1;
    let badgeIndex = 0;

    function getItemWidth() {
        return (badgesWrapper.offsetWidth - (visibleBadges - 1) * gap) / visibleBadges;
    }

    function applyLayout() {
        visibleBadges = window.innerWidth <= 768 ? 2 : 5;
        maxIndex = Math.ceil(totalBadges / visibleBadges) - 1;
        const iw = getItemWidth();
        Array.from(badgesTrack.children).forEach(item => {
            item.style.flex = `0 0 ${iw}px`;
            item.style.width = `${iw}px`;
        });
    }

    const updateBadgeCarousel = () => {
        const iw = getItemWidth();
        badgesTrack.style.transform = `translateX(${-(badgeIndex * visibleBadges * (iw + gap))}px)`;
    };

    applyLayout();

    badgesPrev.addEventListener('click', () => {
        badgeIndex = badgeIndex > 0 ? badgeIndex - 1 : maxIndex;
        updateBadgeCarousel();
    });

    badgesNext.addEventListener('click', () => {
        badgeIndex = badgeIndex < maxIndex ? badgeIndex + 1 : 0;
        updateBadgeCarousel();
    });

    window.addEventListener('resize', () => {
        badgeIndex = 0;
        applyLayout();
        updateBadgeCarousel();
    });
});
</script>
