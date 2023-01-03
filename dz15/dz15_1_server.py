import socket
import logging

logging.basicConfig(level = logging.INFO, filename = 'dz15_1_log.log', format = 'server %(asctime)s - %(levelname)s - %(message)s')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 56000))
sock.listen(10)
print("Server is running, please, press ctrl+c to stop")
while True:
    conn, addr = sock.accept()
    print("Connected:", addr)
    data = conn.recv(1024)
    print(data.decode("UTF-8"))
    if data.decode("UTF-8") == "Hi!":
        logging.info("Greeting from the Server")
        conn.send("Hello!".encode("UTF-8"))
    elif data.decode("UTF-8") == "Who are you?":
        logging.warning("The question from the Client is not substance")
        conn.send("I am Server".encode("UTF-8"))
    elif data.decode("UTF-8") == "Bye!":
        conn.send("See you soon!".encode("UTF-8"))
    else:
        logging.error("No response in Server database")
        conn.send("I don't understand".encode("UTF-8"))
conn.close()
