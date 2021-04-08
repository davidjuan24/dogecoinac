#Lybraries
from os import system
import requests
from bs4 import BeautifulSoup
import datetime
#colores
R = "\033[1;31m"
V = "\033[1;32m"
A = "\033[1;33m"
Z = "\033[1;34m" #BLUE DARK
M = "\033[1;35m" #PURPLE
C = "\033[1;36m" #CYAN OR AQUA
B = "\033[1;37m" #WHITE
DF = "\033[1;0;30m" #BACKGROUND BLACK
default = "\033[39m"
W = "\033[1;107m" #BACKGROND WHITE

def clear():
    if system("clear")==1:
        system("clear")
    else:
        system("cls")


def banner():
    print ("""\033[1;36m
    ██████╗░░█████╗░░██████╗░███████╗
    ██╔══██╗██╔══██╗██╔════╝░██╔════╝
    ██║░░██║██║░░██║██║░░██╗░█████╗░░
    ██║░░██║██║░░██║██║░░╚██╗██╔══╝░░
    ██████╔╝╚█████╔╝╚██████╔╝███████╗
    ╚═════╝░░╚════╝░░╚═════╝░╚══════╝
    """
    )

def banner2():
    d=datetime.datetime.now().strftime("%y-%m-%d")
    loc="https://ipinfo.io"
    src=requests.get(loc)
    data=src.json()
    ip=data['ip']
    region=data['region']
    location=data['loc'].split(",")
    latitude=location[0]
    longitude=location[1]
    country=data['country']
    print ("{}[+]{}{}".format(C,B,d))
    print ("{}website{}:{} dogecoin".format(V, A, R))
    print ("{}[+] Location detected".format(R))
    print ("{}[+]{}ip{} :{}{} ".format(A, C, A, C, ip))
    print ("{}[+]{}region{} :{}{} ".format(A,C,A,C, region))
    print ("{}[+]{}latitude {}:{}{} ".format(A,C,A,C, latitude))
    print ("{}[+]{}longitude {}:{}{} ".format(A,C,A,C, longitude))
    print ("{}[+]{}Country{} :{}{} ".format(A,C,A,C, country))
    print ("              {}[+]{}Creator {}:{}Batcraker ".format(C, V, C, B))
    print ("{}[!]{}Warning {}:{}This script or tool is illegal, use under its responsability.".format(R, A ,V, R) + "\n")
    print ("{}#Spanish\n".format(V))
    print ("{}[!]{}Precaucion {}:{}Este script o herramienta es ilegal, uselo bajo su responsabilidad.".format(R,A,V,R) + "\n")



session = requests.Session()
login = "https://dogecoin.ac/index.php"
try:
    f=open("wallet","r")
    wallet=f.read()
    payload={
        'reference_user_id':'',
        'username': wallet,
    }

except FileNotFoundError:
    clear()
    banner()
    banner2()
    wll=input("\033[1;32mEnter yor wallet(dogecoin): ")
    f=open("wallet", "w")
    wallet=f.write(wll)
    payload={
            'reference_user_id':'',
            'username':wallet,
    }
try:
    clear()
    banner()
    banner2()

    #inicio de session
    session.get(login)
    proces_login=session.post(login, data=payload)
    soup=BeautifulSoup(proces_login.content, 'html.parser')
    title=soup.find_all('title')
    for TITLE in title:
        print (B + TITLE.text)

    print ("\n"+"{}[+]{}Your wallet adress{} : {}{}".format(C,A,C,A,wallet) + "\n")

    #dashboard
    while True:
        dash="https://dogecoin.ac/dashboard.php"
        redirect=session.get(dash)
        html=BeautifulSoup(redirect.content, 'html.parser')
        info=html.find_all('font', id="bal")
        for ballance in info:
            print (V + "\rBallance: " + C + ballance.text + V + " Doge", end='')

except KeyboardInterrupt:
    print ("\n"+"{}[+]{}Gracias por usar mi script".format(Z, B))
    print ("{}[+]{}Thank for use my script".format(Z, B))
