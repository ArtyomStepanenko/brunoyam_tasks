import time
from threading import Thread

def get_thread(thread_name):
	time.sleep(1)
	print(thread_name)

t1 = time.time()

for i in range(5):
	get_thread(i + 1)

print('Time For Sequential Execution: ', time.time() - t1)

threads = [Thread(target = get_thread, args = (i + 1, )) for i in range(5)]

t1 = time.time()

for t in threads:
	t.start()

for t in threads:
	t.join()

print('Time For Parallel Execution: ', time.time() - t1)