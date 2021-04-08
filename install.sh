echo -e "\e[1;36m[+] \e[1;33mActualizando repositorios....."
pkg update -y && pkg upgrade -y > /dev/null 2>&1
echo -e "\e[1;36m[+] \e[1;33mInstalando Python..."
pkg install python -y > /dev/null 2>&1
echo -e "\[1;36m[+] \e[1;33mInstalando Pip....."
pkg install pip -y > /dev/null 2>&1
echo -e "\[1;36m[+] \e[1;33mInstalando requests....."
pip install requests > /dev/null 2>&1
echo -e "\[1;36m[+] \e[1;33mInstalando bs4....."
pip install bs4 > /dev/null 2>&1
echo -e "\[1;36m[+] \e[1;33mInstalando datetime....."
pip install datetime > /dev/null 2>&1