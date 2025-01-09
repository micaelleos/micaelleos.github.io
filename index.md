---
layout: base
title: "Página Inicial"
---

<header class="hero">
  <div class="hero-content">
    <h1>Bem-vindo ao meu site!</h1>
    <p>Explorando produtos de Inteligência Artificial e soluções inovadoras.</p>
  </div>
</header>

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

<section class="about">
  <h2>Sobre Mim</h2>
  <p>Trabalho na área de Inteligência Artificial, criando soluções inovadoras que resolvem problemas reais. Tenho um forte foco em aprendizado de máquina e visão computacional, e sou apaixonado por transformar necessidades em produtos escaláveis e de impacto.</p>
  <a href="/about">Leia mais sobre minha jornada profissional</a>
</section>


