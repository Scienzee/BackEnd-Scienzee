<h1 align="center">Scienzee Back-end</h1>
<p>Criar uma aplicação para a startup Scienzee onde a mesma tenha um design simples e belo, com intuito de mudar a ciencia brasileira</p>
<h4 align="center"> 
	🚧  Status 🚀 Iniciando o projeto  🚧
</h4>

<p align="center">
	<a href="#sobre">Sobre</a> &nbsp;|&nbsp;
    <a href="#Resumo">Resumo</a> &nbsp;|&nbsp;
    <a href="#Observacoes">Observações</a> &nbsp;|&nbsp;
	<a href="#Features">Features</a> &nbsp;|&nbsp;
    <a href="#Tecnologias">Tecnologias</a> &nbsp;|&nbsp;
    <a href="#Rodando">Rodando o Projeto</a> &nbsp;|&nbsp;
	<a href="#autores">Autor(es)</a> &nbsp;|&nbsp;
	<a href="#license">Licença</a>
</p>

<p text-align="justify" id="Resumo">Este repositório tem foco na construção do back-end do sistema, interligado a um banco de dados Postgree facilitando dessa forma a manipulação de seus dados. Seu front-end foi construído pelo framework React oferecido pela Facebook</p>
<p text-align="justify" id="Observacoes">Este sistema faz parte da startup Scienzee, então, ficarei feliz caso você forneça algum feedback, código, estrutura, funcionalidade ou qualquer melhoria que você possa relatar para melhora-lo.Você pode usar este projeto como quiser, seja para estudar, fazer melhorias, você quem manda!.</p>


<h3 id="Feature">:heavy_check_mark: Features</h3>
<p>Funcionalidades para a primeira parte do sistema! Conforme for concluído é somente dar um "X" para identificação das funcionalidades já completas</p>

- [ ] Cadastro de Artigos
- [ ] Cadastro de Notícias
- [ ] Cadastro de Editais
- [ ] Listagem de Artigos (Filtrando de acordo com o gosto do usuários)
- [ ] Listagem de Notícias (Filtrando de acordo com o gosto do usuários)
- [ ] Listagem de Editais (Filtrando de acordo com o gosto do usuários)
- [ ] Denuncia de Artigos
- [ ] Denuncia de Editais
- [ ] Denuncia de Notícias
- [ ] Deletar Artigos
- [ ] Deletar Notícias
- [ ] Deletar Editais
- [ ] Login
- [ ] Reset de senha
- [ ] PDF para impressão de edital


<h3 id="Tecnologias">Tecnologias</h3>
<p>As seguintes ferramentas foram usadas na construção do projeto:</p>

[<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />](https://www.djangoproject.com/)
[<img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray" />](https://reactnative.dev/https://www.django-rest-framework.org/)
[<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />](https://www.python.org/)
[<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />](https://devdocs.io/javascript/)
[<img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white" />](https://www.typescriptlang.org/docs/)
[<img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />](https://www.postgresql.org/)
[<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" />](https://nodejs.org/en/)
<!-- [<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />](https://pt-br.reactjs.org/) -->


<h1 id="Rodando">Rodando o projeto</h1>
<h4>Clonando o projeto</h4>
<p>Dentro do diretório onde o projeto ficará armazenado, abra o terminal.</p>

<h4>Linux</h4>
<blockquote>
  Observação: Foi utilizado a distro Linux Mint(versão 20.1), caso ocorra algum problema na instalação entre em contato!
</blockquote>
<h4>Linux</h4>

``` 
sudo apt-get install python3-venv
```

<h4>Preparando o Projeto</h4>

```
python3 -m venv env
source env/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations Users
python manage.py makemigrations Administration
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```

<h3 id="autores">Autor(es)</h3>

<!-- Coloquem suas fotinhas aqui! -->

 <img style="border-radius: 50%;" src="static/imagens/download.png" width="100px;" alt=""/>
 <sub><b>Camila Adriana</b></sub></a> <a href="www.linkedin.com/in/camila-adriana-gomes-de-jesus-04767b1ba" title="Foto de perfil"></a><br>
Feito com ❤️ pela equipe de desenvolvimento da Scienzee 👋🏽!

[![Twitter Badge](https://img.shields.io/badge/-@camilaA58109563-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/Camila)](https://twitter.com/CamilaA58109563?s=09) [![Linkedin Badge](https://img.shields.io/badge/-Camila-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/Camila/)](https://www.linkedin.com/in/camila-adriana-gomes-de-jesus-04767b1ba/) 

<blockquote>
    Todos os direitos reservados a Scienzee!
</blockquote>