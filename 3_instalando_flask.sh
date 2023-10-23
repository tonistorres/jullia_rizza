MENU_ISNTALL_ENVIRONMENT='
---------------------------------------------------
Install FrameWork Flask
---------------------------------------------------
'
TIME(){
echo "In 2s"
sleep 1
echo "In 1s"
sleep 1    
}

INSTALL_FLASK(){
    echo "$MENU_ISNTALL_ENVIRONMENT"
    pip3 install flask
    echo '********************************'
    python3 -m flask --version
    echo '********************************'
}

INSTALL_FLASK