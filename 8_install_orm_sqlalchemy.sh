source ./4_salvando_dependencias.sh



MENU_VERIFY_PROCESS='
-------------------------
Install ORM Sql Alchemy
É um ORM completo, criado 
com Python para desenvolvedores
de aplicativos, que fornece 
flexibilidade total do SQL,
obtendo um conjunto completo
de padrões de persistência de
nível corporativo bem conhecidos,
que são projetados para acesso a 
banco de dados eficientes e de alto 
desempenho.
-------------------------
'


INSTALL_FLASK_SQLALCHEMY(){
echo "$MENU_VERIFY_PROCESS"    
pip3 install flask-sqlalchemy
pip install --upgrade pip
pip install pymysql
}

INSTALL_FLASK_SQLALCHEMY
SAVE_DEPENDENCE_PROJECT