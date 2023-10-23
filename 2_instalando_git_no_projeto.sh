MENU_ISNTALL_ENVIRONMENT='
---------------------------------------------------
Instalando o Git No projeto
---------------------------------------------------
'
TIME(){
echo "In 2s"
sleep 1
echo "In 1s"
sleep 1    
}

INSTALL_GIT(){
echo "$MENU_ISNTALL_ENVIRONMENT"
TIME
sleep 1
# source .venv/bin/deactivate
# sleep 1
source .venv/bin/activate
sleep 1
git init 
touch .gitignore
}


INSTALL_GIT