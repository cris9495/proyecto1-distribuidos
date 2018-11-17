import socket
import math
import sys
import os
import thread
import subprocess
from sets import Set

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.bind(('192.168.0.14', 9882))
socket1.listen(10)


H = Set()

def program(sc, addr, client):
	global H
	while True:
		operation = sc.recv(1024)
		print(operation)
		if operation == "libre":
			client = sc.recv(1024)
			print("add " + client)
			H.add(client)

		if operation == "needServer":
			envio = H.pop()
			print("send " + envio)
			sc.send(envio)

		if operation == "Reset":
			sc.send("Reset")

		if operation == "successfulProcess":
			cl = sc.recv(1024)
			clientes[cl].send("destroy1")
			time.sleep(0.2)
			clientes[cl].send("successfulProcess")

		if operation == "stoppedProcess":
			cl =sc.recv(1024)
			clientes[cl].send("stoppedProcess")

		if "destroy" == operation:
			print("rmv " + client)
			H.remove(client)
			sc.send("destruir")

clientes = {}

def main():
	print("Servidor corriendo")
	while 1:
		sc, addr = socket1.accept()
		Ip = str(addr[0])
		Puerto = str(addr[1])
		print("recibida conexion de la IP: " + Ip + "puerto: " + Puerto)
		client = sc.recv(1024)
		clientes[client] = sc;
		thread.start_new_thread(program,(sc,addr, client))



main()
sc.close()
socket1.close()
