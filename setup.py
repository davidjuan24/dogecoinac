from os import system

print ("""
Your device is
[01] Linux
[02] Windows
""")
option=input(">> ")

if "01" or "1" in option:
    system("rm dogewin.py")

elif "02" or "2" in option:
    system("del doge.py")