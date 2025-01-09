---
layout: base
title: "Página Inicial"
---

<header class="hero">
  <div class="hero-content">
    <h1>Inovação em IA Generativa e Produtos Digitais</h1>
    <p>Transformando ideias em soluções digitais impactantes com o poder da Inteligência Artificial.</p>
    <a href="#contato" class="btn-contact">Entre em Contato</a> <!-- Botão "Entre em Contato" -->
  </div>
</header>

<section class="about">
  <h2>Sobre Mim</h2>
  <p>Trabalho na área de Inteligência Artificial, criando soluções inovadoras que resolvem problemas reais. Tenho um forte foco em aprendizado de máquina e visão computacional, e sou apaixonado por transformar necessidades em produtos escaláveis e de impacto.</p>
  <a href="/about">Leia mais sobre minha jornada profissional</a>
</section>

<section class="portfolio">
  <h2>Meu Portfólio</h2>
  <div class="portfolio-items">
    <div class="portfolio-item">
      <h3>Projeto 1</h3>
      <p>Descrição breve do projeto, incluindo tecnologias e resultados alcançados.</p>
      <a href="/portfolio/projeto-1">Ver mais</a>
    </div>
    <div class="portfolio-item">
      <h3>Projeto 2</h3>
      <p>Descrição breve do projeto, incluindo tecnologias e resultados alcançados.</p>
      <a href="/portfolio/projeto-2">Ver mais</a>
    </div>
    <!-- Adicione mais itens de portfólio conforme necessário -->
  </div>
</section>

<section class="blog">
  <h2>Últimos Posts do Blog</h2>
  <div class="posts">
    {% for post in site.posts %}
      <div class="post">
        <h3><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h3>
        <p>{{ post.excerpt }}</p>
        <a href="{{ post.url | prepend: site.baseurl }}" class="read-more">Leia mais</a>
      </div>
    {% endfor %}
  </div>
</section>

<!-- Seção de Contato (Exemplo) -->
<section id="contato">
  <h2>Entre em Contato</h2>
  <p>Se você deseja discutir sobre projetos, ideias ou tem alguma dúvida, entre em contato comigo!</p>
  <!-- Adicione seu formulário de contato ou detalhes de contato aqui -->
</section>
