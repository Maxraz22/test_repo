import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 55000))
message = input("Введіть два числа через пробіл і натисніть Enter: ")
sock.send(bytes(message, encoding = "UTF-8"))
data = sock.recv(1024)
sock.close()
print(data.decode("UTF-8"))
