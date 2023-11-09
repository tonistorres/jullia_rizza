
MENU_VERIFY_PROCESS='
-------------------------
Alembic é uma ferramenta de modo texto,
ou seja, temos que executar comando a 
partir de um terminal. Nada de play do
editor de código de sua preferência

O Alembic foi inicialmente desenvolvido
por Mike Bayers, mesmo criador do
SQLAlchemy. Teve sua primeira versão 
lançada em novembro de 2011. 5 anos
após a primeira versão do SQLAlchemy,
em 2006.
* Pode trabalhar em toda a camada DDL;
* Fornece scripts de migração de schemas
 para upgrades e downgrades;
*Suporte a geração de SQL (offline);
* API minimalista.
-------------------------
'


INSTALL_FLASK_MIGRATIONS(){
    echo "$MENU_VERIFY_PROCESS"
    pip3 install alembic
    pip install --upgrade pip
}

INSTALL_FLASK_MIGRATIONS

