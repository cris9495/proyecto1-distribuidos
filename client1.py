import socket
import thread
import time

host = "10.253.21.37"
puerto = 9882
socket1 = socket.socket()


def program():
    global socket1
    socket1.send("libre")
    while True:
        operation = socket1.recv(1024)
        if operation == "destruir":
            print("se destruye")
            thread.exit()






def main():
    socket1.connect((host,puerto))
    thread1 = thread.start_new_thread(program, ())
    print("el thread")
    print(thread1)
    while True:
        raw_input("presiona enter para desbloquear: ")
        socket1.send("destroy")
        cppFile = raw_input("Direccion de archivo cpp: ")
        inputFile = raw_input("Direccion de archivo de entrada: ")

        f = open(cppFile, "rb")
        content = f.read(1024)
        while content:
            print content
            time.sleep(0.2)         

            socket1.send(content)
            content = f.read(1024)
        socket1.send("#")

        cppFile1 = open("archivo.cpp", 'w')
        File = ""
        aux = content
        while aux != "#":
            File += aux
            aux = content
        cppFile1.write(File)
        cppFile1.close()

        if "g++" == operation:
			# archivo cpp
			cppFile1 = open("archivo.cpp", 'w')
			File = ""
			aux = content
			while aux != "#":
				File += aux
				aux = content
			cppFile1.write(File)
			cppFile1.close()

        f = open(inputFile, "rb")
        content = f.read(1024)
        while content:
            print content
            time.sleep(0.2)
            socket1.send(content)
            content = f.read(1024)
        socket1.send("#")
        f.close()


			# Archivo de entrada
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
			os.system("ejecutable.exe < input.in > salida.in")








main()
socket1.close()
