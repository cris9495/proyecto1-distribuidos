import socket
import thread

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



main()
socket1.close()
