MENU_ISNTALL_ENVIRONMENT='
---------------------------------------------------
Creating A Virtual Environment
---------------------------------------------------
'
TIME(){
echo "In 2s"
sleep 1
echo "In 1s"
sleep 1    
}

CREATING_VIRTUAL_ENVIROMENT(){
echo "$MENU_ISNTALL_ENVIRONMENT"
TIME
python3 -m venv .venv && source .venv/bin/activate
}


CREATING_VIRTUAL_ENVIROMENT