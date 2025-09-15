---
layout: base
title: "Home Page"
---

<header class="hero">
    <div class="container">
        <h1>AI Engineer & ML Specialist</h1>
        <p>Architecting intelligent multi-agent systems and generative AI solutions</p>
        <a href="#about" class="btn">Contact Me</a>
    </div>
</header>

<section id="about" class="about">
    <div class="container">
        <h2>About Me</h2>
        <div class="about-content">
            <div class="about-text">
                <p>Hello! I am an electronic engineer with a passion for Artificial Intelligence and technological innovation. I architect multi-agent solutions and design cloud-based AI architectures that deliver measurable business impact. My journey combines expertise in developing practical solutions in Machine Learning and LLMs with a user-centered approach, always striving to turn complex challenges into products that deliver real value. </p>
                <p> My experience allows me to act as a strategic bridge between business needs and the best technical solutions, translating complex requirements into intuitive and powerful tools. Today, I help companies and projects build scalable and integrated AI solutions, from architectural definition to full pipeline implementation — always focusing on efficiency and innovation. </p>
            </div>
            <div class="about-image">
                <img src="/assets/img/profile.jpg" alt="My photo">
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
        <h2>My Specialties</h2>
        <div class="specialty-grid">
            <div class="specialty-item">
                <div class="specialty-icon">🧠</div>
                <h3>Artificial Intelligence</h3>
                <p>Architecture and implementation of complete Machine Learning pipelines and products with LLMs.</p>
            </div>
            <div class="specialty-item">
                <div class="specialty-icon">🤖</div>
                <h3>AI Agents & Multi-Agent Systems</h3>
                <p>LangChain, LangGraph, ReAct patterns, agent orchestration, and complex workflow automation with measurable business impact.</p>
            </div>
            <div class="specialty-item">
                <div class="specialty-icon">☁️</div>
                <h3>Multi-Cloud AI Architecture</h3>
                <p>Enterprise-grade solutions on AWS Bedrock, GCP Vertex AI, and Azure OpenAI Studio with cost optimization and scalability planning.</p>
            </div>
            <div class="specialty-item">
                <div class="specialty-icon">🔍</div>
                <h3>Smart API Integration</h3>
                <p>Development of smart APIs for automation and delivery of scalable solutions.</p>
            </div>
            <div class="specialty-item">
                <div class="specialty-icon">📊</div>
                <h3>Technical and Business Translation</h3>
                <p>Transformation of business requirements into strategic technical solutions.</p>
            </div>
            <div class="specialty-item">
                <div class="specialty-icon">🚀</div>
                <h3>Functional Analysis and Prototyping</h3>
                <p>Requirements gathering and rapid prototyping with integrated artificial intelligence.</p>
            </div>
        </div>
    </div>
</section>

<section id="badges" class="badges">
    <div class="container">
        <h2>My Badges</h2>
        <div class="badges-grid">
            <!-- Embed code from Credly for each badge here -->
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
                    <p style = "margin-top:-120px">Academy Accreditation - Databricks Fundamentals</p>
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
            <!-- Add more embeds as necessary -->
        </div>
    </div>
</section>

<section id="projects" class="projects">
    <div class="container">
        <h2>Featured Projects</h2>
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
    <h2>Latest Blog Posts</h2>
    <div class="posts2">
      {% for post in site.posts %}
        <div class="post2">
          <h3><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h3>
          <p>{{ post.excerpt }}</p>
          <a href="{{ post.url | prepend: site.baseurl }}" class="read-more">Read more</a>
        </div>
      {% endfor %}
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
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            // You can add logic here to send the form
            alert('Thank you for contacting us! We will get back to you soon.');
            contactForm.reset();
        });
    });

document.addEventListener('DOMContentLoaded', () => {
    async function loadProjects() {
        const response = await fetch('projects.md');
        const markdown = await response.text();
        const projects = parseMarkdown(markdown);

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
                View Project</a>
            `;

            projectGrid.appendChild(projectItem);
        });

        // Carousel setup
        const projectWidth = projectGrid.children[0].offsetWidth + 20; // width + gap
        const visibleProjects = window.innerWidth <= 768 ? 1 : 3; // Responsive: 1 project on small screens, 3 on larger ones
        const totalProjects = projects.length;
        const maxIndex = Math.ceil(totalProjects / visibleProjects) - 1;
        let currentIndex = 0;

        // Update the carousel
        const updateCarousel = () => {
            const offset = -(currentIndex * projectWidth * visibleProjects);
            projectGrid.style.transform = `translateX(${offset}px)`;
        };

        // Set up buttons
        prevButton.addEventListener('click', () => {
            currentIndex = (currentIndex > 0) ? currentIndex - 1 : maxIndex;
            updateCarousel();
        });

        nextButton.addEventListener('click', () => {
            currentIndex = (currentIndex < maxIndex) ? currentIndex + 1 : 0;
            updateCarousel();
        });

        // Adjust carousel on window resize
        window.addEventListener('resize', () => {
            currentIndex = 0; // Reset carousel on resize
            updateCarousel();
        });
    }

    function parseMarkdown(markdown) {
        const lines = markdown.split('\n');
        const projects = [];
        let currentProject = {};

        lines.forEach(line => {
            if (line.startsWith('### ')) {
                if (Object.keys(currentProject).length) {
                    projects.push(currentProject);
                }
                currentProject = { name: line.replace('### ', '') };
            } else if (line.startsWith('Descrição: ')) {
                currentProject.description = line.replace('Descrição: ', '');
            } else if (line.startsWith('Imagem: ')) {
                currentProject.image = line.replace('Imagem: ', '');
            } else if (line.startsWith('Link: ')) {
                currentProject.link = line.replace('Link: ', '');
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
