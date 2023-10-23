MENU_ISNTALL_ENVIRONMENT='
---------------------------------------------------
Guardando as Dependencias do Projeto
---------------------------------------------------
'
TIME(){
echo "In 2s"
sleep 1
echo "In 1s"
sleep 1    
}

SAVE_DEPENDENCE_PROJECT(){
    pip3 freeze > requeriments.txt
}

SAVE_DEPENDENCE_PROJECT