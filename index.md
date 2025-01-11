---
layout: base
title: "Página Inicial"
---

<header class="hero">
    <div class="container">
        <h1>Analista Funcional & Especialista em IA</h1>
        <p>Transformando ideias em soluções inovadoras de IA</p>
        <a href="#about" class="btn">Entre em contato</a>
    </div>

</header>

<section id="about" class="about">
    <div class="container">
        <h2>Sobre Mim</h2>
        <div class="about-content">
            <div class="about-text">
                <p>Olá! Sou uma analista funcional apaixonada por desenvolver produtos de IA que transformam negócios e melhoram a vida das pessoas. Com anos de experiência na indústria, combino minha expertise técnica com uma abordagem centrada no usuário para criar soluções inovadoras e eficientes.</p>
                <p>Minha missão é traduzir requisitos complexos em produtos de IA intuitivos e poderosos, sempre buscando o equilíbrio perfeito entre funcionalidade e usabilidade.</p>
            </div>
            <div class="about-image">
                <img src="/assets/img/profile.jpg" alt="Sua foto">
            </div>
        </div>

        <!-- Botões de redes sociais -->
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
        <h2>Minhas Especialidades</h2>
        <div class="specialty-grid">
            <div class="specialty-item">
                <div class="specialty-icon">🧠</div>
                <h3>Inteligência Artificial</h3>
                <p>Desenvolvimento de soluções de IA personalizadas para diversos setores e aplicações.</p>
            </div>
            <div class="specialty-item">
                <div class="specialty-icon">📊</div>
                <h3>Análise Funcional</h3>
                <p>Tradução de requisitos de negócios em especificações técnicas detalhadas.</p>
            </div>
            <div class="specialty-item">
                <div class="specialty-icon">🚀</div>
                <h3>Gestão de Projetos</h3>
                <p>Coordenação eficiente de equipes e recursos para entregar projetos no prazo e dentro do orçamento.</p>
            </div>
            <div class="specialty-item">
                <div class="specialty-icon">🎨</div>
                <h3>UX/UI Design</h3>
                <p>Criação de interfaces intuitivas e atraentes para produtos de IA.</p>
            </div>
        </div>
    </div>
</section>

<section id="projects" class="projects">
    <div class="container">
        <h2>Projetos em Destaque</h2>
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
    <h2>Últimos Posts do Blog</h2>
    <div class="posts2">
      {% for post in site.posts %}
        <div class="post2">
          <h3><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h3>
          <p>{{ post.excerpt }}</p>
          <a href="{{ post.url | prepend: site.baseurl }}" class="read-more">Leia mais</a>
        </div>
      {% endfor %}
    </div>
  </div>
</section>

<script>
    // JavaScript para animações e interatividade
    document.addEventListener('DOMContentLoaded', function() {
        // Animação suave de rolagem para links de navegação
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Animação de entrada para elementos quando entram na viewport
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
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            // Aqui você pode adicionar a lógica para enviar o formulário
            alert('Obrigado pelo seu contato! Retornaremos em breve.');
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

        // Renderiza os projetos
        projects.forEach(project => {
            const projectItem = document.createElement('div');
            projectItem.classList.add('project-item');

            projectItem.innerHTML = `
                <div class="project-image" style="background-image: url('${project.image}'); height: 150px; background-size: cover; border-radius: 8px;"></div>
                <h3>${project.name}</h3>
                <p>${project.description}</p>
                <a href="${project.link}" target="_blank">Ver Projeto</a>
            `;

            projectGrid.appendChild(projectItem);
        });

        // Configuração do carrossel
        const projectWidth = projectGrid.children[0].offsetWidth + 20; // largura + gap
        const visibleProjects = window.innerWidth <= 768 ? 1 : 3; // Responsivo: 1 projeto em telas pequenas, 3 em maiores
        const totalProjects = projects.length;
        const maxIndex = Math.ceil(totalProjects / visibleProjects) - 1;
        let currentIndex = 0;

        // Atualiza o carrossel
        const updateCarousel = () => {
            const offset = -(currentIndex * projectWidth * visibleProjects);
            projectGrid.style.transform = `translateX(${offset}px)`;
        };

        // Configura os botões
        prevButton.addEventListener('click', () => {
            currentIndex = (currentIndex > 0) ? currentIndex - 1 : maxIndex;
            updateCarousel();
        });

        nextButton.addEventListener('click', () => {
            currentIndex = (currentIndex < maxIndex) ? currentIndex + 1 : 0;
            updateCarousel();
        });

        // Ajusta o carrossel ao redimensionar a janela
        window.addEventListener('resize', () => {
            currentIndex = 0; // Reinicia o carrossel ao redimensionar
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
