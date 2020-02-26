import socket

hostname = "192.168.1.5"
port = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((hostname, port))
sock.listen(1)

connection, addr = sock.accept()
print(f"New connection from {addr[0]}")
while 1:
    cmd = input("> ")
    if cmd == "exit":
        break
    connection.send((cmd+"\n").encode("utf-8"))
    output = connection.recv(8192)
    if not output:
        break
    print(output.decode("utf-8"))

connection.close()
print(f"{addr[0]} disconnected.")
