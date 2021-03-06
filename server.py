import socket
import math
import sys
import os
import thread
import subprocess
import time
from sets import Set

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.bind(("192.168.1.78", 9882))
socket1.listen(10)


H = Set()

def program(sc, addr, client):
	global H
	while True:
		operation = sc.recv(1024)
		print(operation)
		if operation == "libre":
			print("add " + client)
			H.add(client)

		if operation == "needServer":
			envio = H.pop()
			clientes[envio].send("process")
			print("send " + envio)
			sc.send("recvMachine")
			time.sleep(0.2)
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
			clientes[cl].send("destroy1")
			time.sleep(0.2)
			clientes[cl].send("stoppedProcess")

		if "destroy" == operation:
			print("rmv " + client)
			H.discard(client)
			sc.send("destruir")

clientes = {}

def main():
	print("Servidor corriendo")
	while 1:
		sc, addr = socket1.accept()
		Ip = str(addr[0])
		Puerto = str(addr[1])
		print("recibida conexion de la IP: " + Ip + "puerto: " + Puerto)
		clientes[Ip + ' ' + Puerto] = sc
		client = sc.recv(1024)
		print client
		clientes[client] = sc;
		thread.start_new_thread(program,(sc,addr, client))



main()
sc.close()
socket1.close()
