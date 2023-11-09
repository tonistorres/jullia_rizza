
MENU_VERIFY_PROCESS='
---------------------------------------------
Iniciando um Sistema de Migrações com Alembic:
1- De acordo com nosso modelo mvc entrar na pasta 
app antes de executar exxe comando.
---------------------------------------------
'



INITIALL_SYSTEM_MIGRATIONS(){
echo "$MENU_VERIFY_PROCESS"
echo ""
echo --------------------------------------------------------
echo -e "\033[31m Você está executando esse Script  \033[m"
echo -e "\033[31m Dentro da Pasta app conforme nosso  \033[m"
echo -e "\033[31m Modelo MVC   \033[m"
read -p "s (sim) e n (não) -->> " CONFIRM
echo --------------------------------------------------------

if [ "$CONFIRM" = s ];then
alembic init migrations
else
echo "O Script não está sendo executado dentro da pasta"
echo -e "\033[31m app conforme Modelo MVC   \033[m"
fi
}

INITIALL_SYSTEM_MIGRATIONS