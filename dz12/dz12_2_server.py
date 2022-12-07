import socket
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 55000))
sock.listen(10)
print("Server is running, please, press ctrl+c to stop")
while True:
    conn, addr = sock.accept()
    print("Connected:", addr)
    data = conn.recv(1024)
    data_decode = data.decode("UTF-8")
    numbers = data_decode.split()
    numbers = [float(i) for i in numbers]
    print("Перше число:", numbers[0])
    print("Друге число:", numbers[1])

    async def sum():
        print("Початок роботи sum")
        await asyncio.sleep(2)
        res1 = numbers[0] + numbers[1]
        print("Закінчення роботи sum")
        return res1

    async def subtract():
        print("Початок роботи subtract")
        await asyncio.sleep(1)
        res2 = numbers[0] - numbers[1]
        print("Закінчення роботи subtract")
        return res2

    async def multipl():
        print("Початок роботи multipl")
        await asyncio.sleep(0)
        res3 = numbers[0] * numbers[1]
        print("Закінчення роботи multipl")
        return res3

    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(sum()), ioloop.create_task(subtract()), ioloop.create_task(multipl())]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)

    msg = ["Сума чисел: " + str(tasks[0].result()), "Різниця чисел: " + str(tasks[1].result()), "Добуток чисел: " + str(tasks[2].result())]
    msg = "\n".join(msg)
    conn.send(bytes(msg, encoding = "UTF-8"))
    conn.close()
