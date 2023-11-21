[Link Top de Pesquisa de Markdown](https://www.markdownguide.org/basic-syntax/#headings)
[Link da Documentação do Flask](https://flask-ptbr.readthedocs.io/en/latest/)

[Youtube Thi Code PlayList Flask Bootstrap](https://www.youtube.com/watch?v=pzsBEuiZ2I4&list=PLR8JXremim5DU70e3x_rYhClgMTzTyv4m&index=1)

> Estruturando Pastas e Arquivos iniciais de um Projeto MVC com Flask

[Youtube Júlia Rizo PlayList Flask ](https://www.youtube.com/watch?v=0iHsyTkyoXo&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX&index=3)

[Alembic API de Operações Documentação](https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.create_foreign_key)

![Logo](./logoFlask.jpeg)


<p>
<b>O que é Flask?</b> É um micro framework. Pense em um Micro-Framework como uma peça de lego. Inicialmente, um projeto criado com o micro-framework possui apenas o básico para funcionar, (normalmente, sistema de rotas), porém, ao decorrer do projeto, podem haver necessidades para utilização de outros recursos como, conexão de banco de dados, sistemas de templates, envio de email, etc. A partir desta necessidade, novas bibliotecas são “encaixadas” no projeto, como uma estrutura de lego.
</p>

<p>
 Lançado em 2010 e desenvolvido por Armin Ronacher, o Flask é um micro-framework destinado principalmente a pequenas aplicações com requisitos mais simples, como por exemplo, a criação de um site básico.
 </p>

 <p>
 <b>Dica Importante:</b>
 Para criar um projeto MVC inicial com Flask, seguimos a dica da tecnóloga Julia Rizzo como descrito no link conforme disposto na parte superior do REDEAME.md, composto com 07(sete) passos que foram escritor em linguagem shell script conforme detalhamento logo abaixo diposto:
 <br>
  <b>PRIMEIRO PASSO:</b>
  <i>
    Iremos executar o arquivo <strong>1_criando_ambiente_virtual.sh</strong> -> reponsável por configurar e criar o ambiente virtual python do projeto.
  </i>
  <br>
  <b>SEGUNDO PASSO:</b>
  <i>
    Iremos executar o arquivo <strong>2_instalando_git_no_projeto.sh</strong> -> reponsável por fazer o controle de versionamento da aplicação de forma local e na núvem (github).
  </i>
 <b>TERCEIRO PASSO:</b>
  <i>
    Iremos executar o arquivo <strong>3_instalando_flask.sh</strong> -> reponsável por fazer a instalação do microframework na pasta do projeto dentro do ambiente virtual setado.
  </i>

  <b>QUARTO PASSO:</b>
  <i>
    Iremos executar o arquivo <strong>4_salvando_dependências.sh</strong> -> reponsável por salvar todas libs do projeto dentro de uma arquivo txt chamado <strong>requeriments.txt</strong>.
  </i>

  <b>QUINTO PASSO:</b>
  <i>
    Iremos executar o arquivo <strong>5_run_server.sh</strong> -> reponsável executar o servidor  (localhost) do flask onde iremos desenvolver a aplicação antes de hospedar na núvem.  </i>


  <b>SEXTO PASSO:</b>
  <i>
    Iremos executar o arquivo <strong>6_limpando_port_5000.sh</strong> -> reponsável caso a aplicação esteja rodando em portas diferentes podemos stopar e iniciar a aplicação novamente.  </i>
 
  <b>SÉTIMO PASSO:</b>
  <i>
    Iremos executar o arquivo <strong>7_initiall_aplication_flask.sh</strong> -> reponsável por criar a estrutura MVC (grupo de pastas e sub-pastas iniciais do projeto), e criar e escrever arquivos iniciais de configuração do projeto e roda o projeto inicial hellow world.  </i>   

 </p>

[Vídeo Exemplo Organizando aplicação no modelo MVC](https://www.youtube.com/watch?v=0iHsyTkyoXo&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX&index=3)

<h4>Organizando a aplicação no modelo MVC</h4>
<p> 

* 1º vamos criar a pasta principal a nomearei de <strong><i>app</i></strong><br>

* 2º Dentro da pasta principal <strong>app</strong>, iremos criar as seguintes sub-pastas:<br>
    
    * models - iremos tercerizar essa camada para orm sqlalchemy;
    * controllers - onde ficará a lógica da aplicação;
    * static - onde ficarão os arquivos estáticos (css) ...
    * tempaltes - onde ficarão os arquivos html.
 <p>

 <p>
 <b>Observação 1:</b> No flask temos um padrão que toda pasta contendo arquivo html se chamam <strong>templates</strong> e a pasta que contém arquivos estáticos<b>(css)</b> se chama <strong>static</strong>
 </p>


<h4>Ilustração:</h4>

 ![Logo](./app.png)

<p>
<b>Observação 2:</b> dentro da pasta principal <strong>app</strong> criaremos um arquivo com o nome <strong>__init__.py</strong> utilizamos esse procedimento de criar esse arquivo quando iremos treabalhar com módulos dentro do python. O  <strong>__init__.py</strong> aqui explicitádo está indicando que a pasta <b>app</b>
 é o módulo principal e que no futuro teremos sub-módulos dentro da pasta  <strong>app</strong> onde cda uma das pastas terão  <strong>__init__.py</strong> com exceção da pasta <i>templates e static</i>
</p>

<p>
 O <strong>__init__.py</strong> <b><i>principal</i></b> que está dentro da pasta <b><i>app</i></b> conterá as configurações principais do flask.
</p>


<h4>Ilustração arquivo <strong>__init__.py da pasta app</strong>:</h4>

![Logo](./app__init__.png)

 ```py
 
from flask import Flask


app = Flask(__name__)

# importando o módulo controllers para o módulo  
# principal de execução
from app.controllers import default
 ```


<p>
<b>Observação 3:</b> No arquivo <strong>run.py</strong>
ficará a lógica para iniciar a execução da aplicação.
<p>


![local run.py](./run.png)


```py
# Neste arquivo ficará a lógica para startar
# a aplicação

from app import app


if __name__ =="__main__":
    app.run()


```
<p>Observação 4: a camada de <b>controllers</b> será conterá os arquivos de lógica da aplicação, como exemplo inicial temos o arquivos (__init__.py) indicando que é um sub-módulo de <b>app</b> dentro do python e temos o arquivo (default.py) com um exemplo de hello word na rota index da aplicação. </p>

![controllers](./controllers.png)
```py
from app import app 

@app.route("/")
def index():
    return f" 🤟 Hellow World"

```


 <h4>Desenvolvedor Sql Alchemy e Alembic  Mike Bayers</h4>

![Logo](./Mike_Bayers.png)

[Link Blog Mike Bayers](https://techspot.zzzeek.org/)

 <p>

[Youtube Júlia Rizo Falsk SQlAlchemy ](https://www.youtube.com/watch?v=R3nS66dgo2w&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX&index=4)
 
 ![Logo](./flaskalch.jpeg)

 <strong>O que é Flask SqlAlchemy?</strong><i> É um ORM completo, criado com Python para desenvolvedores de aplicativos, que fornece flexibilidade total do SQL, obtendo um conjunto completo de padrões de persistência de nível corporativo bem conhecidos, que são projetados para acesso a banco de dados eficientes e de alto desempenho.</i><br>
 Ele permite que você crie modelos de dados e consultas de uma maneira que se sente como classes e declarações normais do python.
 </p>

<p>
<b>Por que usar o SQL Alchemy?</br>
<i> * Abstrair seu código de SQL;</i><br>
<i> * Aproveitar declarações e tipos comuns instruções SQL sejam criadas de forma eficiente;</i><br>
<i> * Evitar ataques comuns, como ataque de sql injection;</i><br>
<i> * É um banco extensível (trabalha com Oracle, Postgres, Mysql etc.)</i><br>
<i> * Trabalha em dois modos diferentes (Core e ORM).</i><br>
</p>

[Sql Alchemy ORM 9min e 22seg Dunossauro](https://www.youtube.com/watch?v=rBIksyGY4_E)

<h4>Características do ORM SQL Alchemy:</h4>

<p>
<i> * Se parece tradicionalmente com outro ORMs;</i><br>
<i> * Fornece uma grande camada de abstração do SQL, porém, converte tudo para a camada do core;</i><br>
<i> * Trata tabelas e dados com a abstração de classes e objetos;</i><br>
<i> * Pode ser usada com o Core para camadas mais abstratas.</i><br>
</p>

<h4>Tabela de tipos:</h4>

 ![Table type](./tabletype.png)


 <p><strong>Instalação:</strong>
 </br>
  <i>Já setado no ambiente virtual do módulo python a ser trabalhado, digite o seguinte comando:</i> <strong>pip3 install flask-sqlalchemy</strong> 
 </p>


<h4>SqlAlchemy Core:</h4>
<p>
Os tipos de dados e as abstrações necessárias para executar a API de operações estão no SQL Alchemy Core. Também podemos dizer que é uma meneira pythonica de representar seus dados sem perder o sotaque do SQL.<br>
Focado diretamente no banco de dados e seu esquema. Proporciona a base para o ORM.
</p>

<h1>criando nossa primeira tablea com SQL CORE</h1>



 <p>
  <strong>
    Modelo do Banco de Dados a ser Trabalhado no Projeto:
  <strong>
  </br>

  ![Logo](./model.png)

 </p>

[DOCUMENTAR DEPOIS A PARITR 23 min : 56 seg ](https://www.youtube.com/watch?v=yQtqkq9UkDA&t=14s)


<h1>O que é o Alembic?</h1>

<p>
<b>O Alembic é uma ferramenta de modo texto, ou seja, temos que executar comando a partir de um terminal. Nada de play do editor de código de sua preferência</b>
</p>

<p>
O <strong>Alembic</strong> foi inicialmente desenvolvido por Mike Bayers, mesmo criador do SQLAlchemy. Teve sua primeira versão lançada em novembro de 2011. 5 anos após a primeira versão do SQLAlchemy, em 2006.
</br>
 * Pode trabalhar em toda a camada DDL;
</br>
* Fornece scripts de migração de schemas para upgrades e downgrades;
</br>
*Suporte a geração de SQL (offline);
</br>
* API minimalista.
</p>

<p>
<strong>Instalação:<strong> Se preferir execute o script sheel 9_instalando_alembic.sh a partir do terminal executando o comando a baixo explicitado e o script irá instalar o alembic de forma automática:<br>

```sh
bash 9_instalando_alembic.sh
```
</p>

![Instal Alembic](./alembic.png)


<p><strong>Execução:</strong></p>

<p>
Entre na pasta do projeto, em nosso caso o diretório(app) e execute o comando abaixo conforme ilustração:
<i>O comando abaixo init nos diz que iremos inicializar um sistema de migrações dentro da nossa aplicação</i>
<p>

![Inicializando Pasta de migrações](./init.png)

<p>
Se preferir entre na pasta app por meio do terminal e execute o script 10_inicio_sistema_migracao.sh conforme explicitado logo abaixo:<br>

```sh
cd app 
bash 10_inicio_sistema_migracao.sh
```
</p>

<p>Estrutura Criada no Projeto pelo comando<strong><i>alembic init migrations </i></strong></p>

![Estrutura de pasta do App - Foco Migrations](./structure.png)

<h3>Arquivos Importante Criados Juntos a Estrutura de Pastas:</h3>


<p>
<strong>* alembic.init</strong></br>
<i>O script escrito no alembic.init é uma arquivo criado de forma automática, portanto, genérico que consiste numa configuração para um único banco de Dados.</i>

![alembic.ini](./alembicini.png)

<p>Conteúdo do script alembic.ini, somente os comandos base (contendo as configuraçẽos principais) para acoplá-lo ao ORM Sql Alchemy </p>

```py
# A generic, single database configuration.
'''
Esse comentário indica que essa é uma configuração genérica, que irá 
funcionar em um único banco de dados.
'''


[alembic]
# path to migration scripts
'''
Em trocados e miudos, o alembic pergunta onde estão os scripts criados para execução do alembic. Em nosso caso 
dentro em app numa sub-pasta por nome migrations
'''
script_location = app/migrations

'''
Alembic pergunta de onde eu preciso partir para encontrar 
o caminho passado em script_location - a resposta é a partir
do diretório raiz ponto ( . ) 
'''
prepend_sys_path = .


version_path_separator = os  

'''
Qual a uri do meu banco de dados
'''
sqlalchemy.url = mysql+pymysql://root:1020@localhost:3306/dbtwitterjulia

```
</p>

<p>
Dentro da estrutura de pasta e arquivos criado pelo comando:

```sh
alembic init migrations
```
temos o arquivo env.py que é onde são feitas as configurações das migrações.<br>
Corpo do arquivo env.py contido dentro da pasta migrations de acordo com nosso modelo MVC.


```py
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = None

'''
ofline ele gera um sql para usarmos esse código depois em nosso banco de dados

'''


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()
'''
Uma migração online que dizer que no momento que eu pedir para rodar a migraçao ele irá rodar essa migração no banco de dados

'''

def run_migrations_online() -> None:

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

```

</p>



[Canal Dunossauro Vídeo 34min:21s](https://www.youtube.com/watch?v=yQtqkq9UkDA&t=14s)

<h4>Tudo Pronto Criando nossa primeira migração :</h4>
-  Comando que criar um versionamento na pasta <i>migrations</i> conforme configurações aqui explicitada logo no readme.mb acima.


![Comando cria um versionamento](./revision.png)

<h4>Corpo do Script (conteúdo do versionamento):</h4>


[Canal Dunossauro Vídeo 37min Funções upgrade e downgrade](https://www.youtube.com/watch?v=yQtqkq9UkDA&t=14s)

```py
"""primeira

Revision ID: 41244e6b200b
Revises: 
Create Date: 2023-11-04 08:51:40.598200

"""
from typing import Sequence, Union

# Api de operações DDL 
from alembic import op


import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41244e6b200b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# (Explicação Youtube em 37 min)[https://www.youtube.com/watch?v=yQtqkq9UkDA&t=14s]

# upgrade -> é a função que aplica a migração, ou seja, como é que essa migração será aplicada de fato.
# Exemplo: Quero criar uma tabela, quero modificar ... 


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(),primary_key=True),
        sa.Column('username', sa.String(length=50), nullable=False),
        sa.Column('password', sa.String(length=10),nullable=False),
        sa.Column('name', sa.String(length=60),nullable=False),
        sa.Column('email', sa.Integer(length=100))
        
    )

# downgrade -> quero excluir uma tabela, remover a coluna 
def downgrade() -> None:
    op.drop_table(
        'user'
    )


```
[Canal Dunossauro Vídeo 46min 30seg Aplicando Migrações](https://www.youtube.com/watch?v=yQtqkq9UkDA&t=14s)

<h4>Aplicando migração:</h4>

<p>
No arquivo alembic.ini na pasta raiz iremos fazer configuração da URI do banco de dados que estamos trabalhando.<br>

![Configurando URI alembic.ini](./config_alembicini.png)
</p>

<h4>Executando codigo que startar migração:</h4>

[Explicação do comando alembic upgrade head  48min 55seg ](https://www.youtube.com/watch?v=yQtqkq9UkDA&t=14s)

```sh
# head -> Executa todas as migrações relacionadas a função upgrade
alembic upgrade head
```
<h4>Desfazendo a migração comando:</h4>

```sh
# Executa todas a migrações relacionada a função donwgrade 
alembic downgrade base
```

<h4>Vê o Histórico comando:</h4>

```sh
# histórico da execução das migrações
alembic history
```
[Executando SQL Personalizado com Alembic ](https://learnbatta.com/blog/alembic-ddl-operations/)

<h1> Para esse exemplo estudar esse link</h1>

[relacionamento de tabelas com sql gerar as migrações de relacionamento](https://www.udemy.com/course/curso-mysql/learn/lecture/5078898?start=570#overview)
```sh
op.execute('create view product_view as select * from product')
```

<h1>Da prosseguimento a partir daqui </h1>

[Dunossauro 52min ](https://learnbatta.com/blog/alembic-ddl-operations/)