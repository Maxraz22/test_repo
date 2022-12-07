import concurrent.futures
import time

def fac(x):
    if x == 0:
        return 1
    return fac(x - 1) * x


x1 = 100
x2 = 200
x3 = 300
x4 = 400
x5 = 500

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as thread:
        start_thread = time.time()
        fac_1 = thread.submit(fac, x1).result()
        fac_2 = thread.submit(fac, x2).result()
        fac_3 = thread.submit(fac, x3).result()
        fac_4 = thread.submit(fac, x4).result()
        fac_5 = thread.submit(fac, x5).result()
        finish_thread = time.time() - start_thread

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as process:
        start_process = time.time()
        fac_1 = process.submit(fac, x1).result()
        fac_2 = process.submit(fac, x2).result()
        fac_3 = process.submit(fac, x3).result()
        fac_4 = process.submit(fac, x4).result()
        fac_5 = process.submit(fac, x5).result()
        finish_process = time.time() - start_process

    if finish_thread < finish_process:
        print("Оптимальнішим є ThreadPoolExecutor зі швидкістю виконання:", finish_thread)
    elif finish_thread > finish_process:
        print("Оптимальнішим є ProcessPoolExecutor зі швидкістю виконання:", finish_process)
    else:
        print("ThreadPoolExecutor та ProcessPoolExecutor є рівнозначними за оптимальністю зі швидкістю виконання:", finish_thread)

