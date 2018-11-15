import socket
import math
import sys
import thread

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.bind(('10.253.21.37', 9882))
socket1.listen(10)

def program(sc, addr):
	while True:
		operation = sc.recv(1024)
		print(operation)
		if "g++" == operation:
			# archivo cpp
			cppFile = open("archivo.cpp", 'w')
			File = ""
			aux = sc.recv(1024)
			while aux != "#":
				File += aux
			cppFile.write(File)
			cppFile.close()
			# Archivo de entrada
			entrada = open("input.in", 'w')
			File = ""
			aux = sc.recv(1024)
			while aux != "#":
				File += aux
			entrada.write(File)
			entrada.close()
			p1 = Popen(["g++", "archivo.cpp", "-o", "ejecutable.exe"])
			

		if "destroy" == operation:
			sc.send("destroy")


def main():
	print("Servidor corriendo")
	while 1:
		sc, addr = socket1.accept()
		print("recibida conexion de la IP: " + str(addr[0]) + "puerto: " + str(addr[1]))
		thread.start_new_thread(program,(sc,addr))



main()
sc.close()
socket1.close()
