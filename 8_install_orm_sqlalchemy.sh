source ./4_salvando_dependencias.sh

INSTALL_FLASK_SQLALCHEMY(){
pip3 install flask-sqlalchemy
pip install --upgrade pip
pip install pymysql
}

INSTALL_FLASK_SQLALCHEMY
SAVE_DEPENDENCE_PROJECT