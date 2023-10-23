# https://stackoverflow.com/questions/73309491/port-xxxx-is-in-use-by-another-program-either-identify-and-stop-that-program-o

MENU_VERIFY_PROCESS='
--------------
VERIFY PROCESS
--------------
'

MENU_STOP_PROCESS='
-------------------------------
Matando processo na porta 5000
-------------------------------
'

TIME(){
echo "In 2s"
sleep 1
echo "In 1s"
sleep 1    
}



VERIFY_PROCESS_RUN(){
echo "$MENU_VERIFY_PROCESS"
TIME    
lsof -i :5000
STOP_PROCCESS_IN_PORT_5000
}

STOP_PROCCESS_IN_PORT_5000(){
echo "$MENU_STOP_PROCESS"
read -p "Digite o Nº PID -->> " PID
kill -9 $PID
lsof -i :5000        
}


VERIFY_PROCESS_RUN