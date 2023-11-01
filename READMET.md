






 <p>
 Flask- Flask-Migrate é uma extensão que lida com migrações de banco de dados SQLAlchemy para aplicativos Flask usando Alembic. As operações do banco de dados são disponibilizadas por meio da interface de linha de comando do Flask.
</p>
<p>
Por que usar Flask-Migrate vs. Alembic diretamente? 
Flask-Migrate é uma extensão que configura o Alembic da maneira adequada para trabalhar com seu aplicativo Flask e Flask-SQLAlchemy. Em termos de migrações reais de banco de dados, tudo é feito pelo Alembic para que você obtenha exatamente a mesma funcionalidade.
</p>


[Documentação: Sobre Migrações no Flask](https://flask-migrate.readthedocs.io/en/latest/)

[Canal Youtube: Sobre Migrações no Flask](https://www.youtube.com/watch?v=tJZjniFdaIw&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX&index=5)


<h4>Instalação</h4>
<h5><i>Instale o Flask-Migrate com pip :</i><h5>

<strong>pip install Flask-Migrate</strong>



[Documentação: Sobre Flask Script](https://flask-script.readthedocs.io/en/latest/)

[Canal Youtube: Sobre Flask Script 1 min 20 seg ](https://www.youtube.com/watch?v=tJZjniFdaIw&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX&index=5)


<h1>Aviso</h1>

<p>
Embora os mantenedores estejam dispostos a fundir PRs, eles não estão desenvolvendo recursos ativamente. A partir do Flask 0.11, o Flask inclui uma ferramenta CLI integrada e que pode atender melhor às suas necessidades.
</p>

<p>
A extensão Flask-Script fornece suporte para escrever scripts externos no Flask. Isso inclui a execução de um servidor de desenvolvimento, um shell Python personalizado, scripts para configurar seu banco de dados, cronjobs e outras tarefas de linha de comando que pertencem a fora do próprio aplicativo web.
</p>

<p>
Flask-Script funciona de maneira semelhante ao próprio Flask. Você define e adiciona comandos que podem ser chamados da linha de comando para uma Managerinstância.
</p>

<h2>Instalando Flask</h2> 

<h4>Instale com pip e easy_install :<h4>

<strong>pip3 install Flask-Script<strong>

