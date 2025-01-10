---
layout: base
title: "Página Inicial"
---

<header class="hero">
    <div class="container">
        <h1>Analista Funcional & Especialista em IA</h1>
        <p>Transformando ideias em soluções inovadoras de IA</p>
        <a href="#contact" class="btn">Entre em contato</a>
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
        <div class="project-grid">
            <div class="project-item">
                <div class="project-image" style="background-image: url('https://via.placeholder.com/300x200');"></div>
                <div class="project-info">
                    <h3>Sistema de Recomendação de IA</h3>
                    <p>Desenvolvimento de um sistema de recomendação personalizado para uma plataforma de e-commerce.</p>
                </div>
            </div>
            <div class="project-item">
                <div class="project-image" style="background-image: url('https://via.placeholder.com/300x200');"></div>
                <div class="project-info">
                    <h3>Chatbot de Atendimento ao Cliente</h3>
                    <p>Criação de um chatbot inteligente para melhorar o suporte ao cliente de uma grande empresa de telecomunicações.</p>
                </div>
            </div>
            <div class="project-item">
                <div class="project-image" style="background-image: url('https://via.placeholder.com/300x200');"></div>
                <div class="project-info">
                    <h3>Análise Preditiva de Manutenção</h3>
                    <p>Implementação de um sistema de manutenção preditiva baseado em IA para uma indústria automotiva.</p>
                </div>
            </div>
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

<section id="contact" class="contact">
    <div class="container">
        <h2>Entre em Contato</h2>
        <form class="contact-form" id="contact-form">
            <div class="form-group">
                <label for="name">Nome</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">E-mail</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="message">Mensagem</label>
                <textarea id="message" name="message" required></textarea>
            </div>
            <button type="submit" class="btn">Enviar Mensagem</button>
        </form>
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
</script>
