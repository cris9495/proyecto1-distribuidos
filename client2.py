import socket
import thread
import time
import sys
import os
import subprocess
import math

hostCentralServer = "192.168.0.14"
puertoCentralServer = 9882

host = "192.168.0.14"
port = 9884

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sServer.bind((host, port))
sServer.listen(10)


def ejecution():
    global socket1
    while True:
        sc, addr = sServer.accept()
        print("Conectado con el cliente: IP: " + addr[0] + " PORT: " + str(addr[1]))
        # recibiendo el archivo cpp

        cppFile = open("archivo.cpp", 'w')
        File = ""
        aux = sc.recv(1024)
        while aux != "#":
            File += aux
            aux = sc.recv(1024)
        cppFile.write(File)
        cppFile.close()
        # recibiendo el archivo cpp

        entrada = open("input.in", 'w')
        File = ""
        aux = sc.recv(1024)
        while aux != "#":
            File += aux
            aux = sc.recv(1024)
        entrada.write(File)
        entrada.close()
        p1 =  subprocess.Popen(["g++", "archivo.cpp", "-o", "ejecutable.exe"])
        p1.communicate()
        os.system("ejecutable.exe < input.in > salida.out")


def program():
    global socket1
    socket1.send("libre")
    time.sleep(0.2)
    socket1.send(host + ' ' + str(port))
    thread.start_new_thread(ejecution,())
    while True:
        operation = socket1.recv(1024)
        if operation == "destruir":
            print("se destruye")
            thread.exit()



def main():
    socket1.connect((hostCentralServer,puertoCentralServer))
    thread1 = thread.start_new_thread(program, ())
    print("el thread: " + str(thread1))
    while True:
        raw_input("presiona enter para desbloquear: ")
        socket1.send("destroy")
        cppFile = raw_input("Direccion de archivo cpp: ")
        inputFile = raw_input("Direccion de archivo de entrada: ")

        # solicitando Servidor

        socket1.send("needServer")
        resultado = socket1.recv(1024)
        IPPUERTO = resultado.split(" ")
        socket2 = socket.socket()
        socket2.connect((IPPUERTO[0], int(IPPUERTO[1])))

        # Enviando archivo cpp

        f = open(cppFile, "rb")
        content = f.read(1024)
        while content:
            print content
            time.sleep(0.2)
            socket2.send(content)
            content = f.read(1024)
        socket2.send("#")

        # Enviando entrada

        f = open(inputFile, "rb")
        content = f.read(1024)
        while content:
            print content
            time.sleep(0.2)
            socket2.send(content)
            content = f.read(1024)
        socket2.send("#")
        f.close()


main()
sc.close()
sServer.close()
socket1.close()
