
MENU_VERIFY_PROCESS='
--------------
FLASK MIGRATIONS
--------------
'


INSTALL_FLASK_MIGRATIONS(){
    echo "$MENU_VERIFY_PROCESS"
    pip3 install Flask-Migrate
    pip3 install alembic
    pip install --upgrade pip

}

INSTALL_FLASK_MIGRATIONS

